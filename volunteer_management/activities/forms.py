from django import forms
from django.contrib.auth.models import User
from .models import Activity, Registration
from django.utils.translation import gettext_lazy as _

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password', 'email']

class ActivityForm(forms.ModelForm):
    date = forms.DateField(widget=forms.DateInput(format='%d/%m/%Y'), input_formats=['%d/%m/%Y'])

    class Meta:
        model = Activity
        fields = ['title', 'description', 'date', 'location', 'available_slots']
        labels = {
            'title': _('Title'),
            'description': _('Description'),
            'date': _('Date (DD/MM/YYYY)'),
            'location': _('Location'),
            'available_slots': _('Available Slots'),
        }

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = []

# Druhý formulář log in log out
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password', 'email']

class ActivityForm(forms.ModelForm):
    date = forms.DateField(widget=forms.DateInput(format='%d/%m/%Y'), input_formats=['%d/%m/%Y'])

    class Meta:
        model = Activity
        fields = ['title', 'description', 'date', 'location', 'available_slots']

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = []

class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Username', max_length=254)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
