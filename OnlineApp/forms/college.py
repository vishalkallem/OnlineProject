from django import forms
from OnlineApp.models import *


class AddCollege(forms.ModelForm):
    class Meta:
        model = College
        exclude = ['id']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the college name'}),
            'location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the college location'}),
            'acronym': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the college acronym'}),
            'contact': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter the college email id'}),
        }


class UpdateCollege(forms.ModelForm):
    class Meta:
        model = College
        exclude = ['id']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the college name'}),
            'location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the college location'}),
            'acronym': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the college acronym'}),
            'contact': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter the college email id'}),
        }
