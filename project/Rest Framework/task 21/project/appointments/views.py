from django.shortcuts import render
import stripe
import paypalrestsdk
from django.conf import settings
from django.shortcuts import render, get_object_or_404, redirect
from .models import Doctor, Appointment
from .forms import AppointmentForm, StripePaymentForm

stripe.api_key = settings.STRIPE_SECRET_KEY

paypalrestsdk.configure({
    "mode": "sandbox",
    "client_id": settings.PAYPAL_CLIENT_ID,
    "client_secret": settings.PAYPAL_CLIENT_SECRET,
})

def book_appointment(request, doctor_id):
    doctor = get_object_or_404(Doctor, id=doctor_id)
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = Appointment.objects.create(
                doctor=doctor,
                patient_name=form.cleaned_data['patient_name'],
                appointment_date=form.cleaned_data['appointment_date'],
            )
            return redirect('make_payment', appointment_id=appointment.id)
    else:
        form = AppointmentForm()
    return render(request, 'appointments/book.html', {'doctor': doctor, 'form': form})


def make_payment(request, appointment_id):
    appointment = get_object_or_404(Appointment, id=appointment_id)
    if request.method == 'POST':
        form = StripePaymentForm(request.POST)
        if form.is_valid():
            try:
                stripe.Charge.create(
                    amount=5000,
                    currency='usd',
                    source=form.cleaned_data['stripeToken'],
                    description=f"Payment for appointment with Dr. {appointment.doctor.name}",
                )
                appointment.is_paid = True
                appointment.save()
                return render(request, 'appointments/success.html', {'appointment': appointment})
            except stripe.error.StripeError:
                return render(request, 'appointments/error.html', {'error': "Stripe payment failed!"})
    else:
        form = StripePaymentForm()
    return render(request, 'appointments/stripe_payment.html', {
        'form': form,
        'stripe_publishable_key': settings.STRIPE_PUBLISHABLE_KEY,
        'appointment': appointment,
    })


def paypal_payment(request, appointment_id):
    appointment = get_object_or_404(Appointment, id=appointment_id)
    if request.method == 'POST':
        payment = paypalrestsdk.Payment({
            "intent": "sale",
            "payer": {"payment_method": "paypal"},
            "redirect_urls": {
                "return_url": "http://localhost:8000/payment/success/",
                "cancel_url": "http://localhost:8000/payment/cancel/",
            },
            "transactions": [{
                "item_list": {
                    "items": [{
                        "name": f"Appointment with Dr. {appointment.doctor.name}",
                        "sku": "001",
                        "price": "50.00",
                        "currency": "USD",
                        "quantity": 1,
                    }]
                },
                "amount": {"total": "50.00", "currency": "USD"},
                "description": f"Payment for appointment with Dr. {appointment.doctor.name}",
            }],
        })
        if payment.create():
            for link in payment.links:
                if link.rel == "approval_url":
                    return redirect(link.href)
        else:
            return render(request, 'appointments/error.html', {'error': "PayPal payment creation failed!"})
    return render(request, 'appointments/paypal_payment.html', {'appointment': appointment})
