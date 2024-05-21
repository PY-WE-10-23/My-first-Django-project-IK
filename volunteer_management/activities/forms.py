from django import forms
from .models import Activity, Registration

class ActivityForm(forms.ModelForm):
    class Meta:
        model = Activity
        fields = ['title', 'description', 'date', 'available_slots']

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = []
