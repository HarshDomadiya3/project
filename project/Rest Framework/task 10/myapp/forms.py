from django import forms

class OTPForm(forms.Form):
    phone_number = forms.CharField(max_length=15)
    otp = forms.CharField(max_length=6)
