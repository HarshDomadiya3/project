from django import forms

class AppointmentForm(forms.Form):
    patient_name = forms.CharField(max_length=100)
    appointment_date = forms.DateTimeField(widget=forms.TextInput(attrs={'type': 'datetime-local'}))


class StripePaymentForm(forms.Form):
    stripeToken = forms.CharField(widget=forms.HiddenInput())
