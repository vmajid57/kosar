from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.validators import RegexValidator


class UserRegistrationForm(UserCreationForm):
    full_name = forms.CharField(max_length=101)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+999999999'. Up to 15 digits"
                                         " allowed.")
    phone_number = forms.CharField(validators=[phone_regex], max_length=17,)
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'full_name', 'phone_number', 'email', 'password1', 'password2']
