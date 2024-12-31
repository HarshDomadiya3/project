from django.shortcuts import render
from django.http import HttpResponse
from .forms import OTPForm
from twilio.rest import Client
from django.conf import settings
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')


otp = None  


def send_otp(phone_number):
    otp = "123456" 
    client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
    message = client.messages.create(
        body=f"Your OTP code is {otp}",
        from_=settings.TWILIO_PHONE_NUMBER,
        to=phone_number
    )
    return otp


def request_otp(request):
    global otp
    if request.method == 'POST':
        form = OTPForm(request.POST)
        if form.is_valid():
            phone_number = form.cleaned_data['phone_number']
            otp = send_otp(phone_number) 
            return HttpResponse("OTP sent to your phone number.")
    else:
        form = OTPForm()
    return render(request, 'otp_form.html', {'form': form})


def verify_otp(request):
    global otp
    if request.method == 'POST':
        form = OTPForm(request.POST)
        if form.is_valid():
            entered_otp = form.cleaned_data['otp']
            if entered_otp == otp: 
                return HttpResponse("OTP Verified Successfully!")
            else:
                return HttpResponse("Invalid OTP. Please try again.")
    else:
        form = OTPForm()
    return render(request, 'otp_verify.html', {'form': form})

def home(request):
    return HttpResponse("Welcome to the home page after login!")
