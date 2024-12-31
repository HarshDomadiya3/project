from django import forms

class AddressForm(forms.Form):
    address = forms.CharField(label="Enter Address", max_length=255, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter a location or address',
    }))
