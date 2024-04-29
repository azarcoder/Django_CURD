from django import forms
from . models import RegisterForm

#class name here is user defined
class MyregisterForm(forms.ModelForm):
    class Meta:
        model = RegisterForm
        fields = ['name', 'age', 'address', 'contact', 'email']