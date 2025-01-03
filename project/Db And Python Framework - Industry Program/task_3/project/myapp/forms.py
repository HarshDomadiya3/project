from django import forms

class MyForm(forms.Form):
    name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(required=True)
    age = forms.IntegerField(min_value=1, max_value=100, required=True)
