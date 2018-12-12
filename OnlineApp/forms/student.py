from django import forms
from OnlineApp.models import *


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        exclude = ['id', 'dob', 'college']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email id'}),
            'db_folder': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your db_folder name'}),
            'dropped_out': forms.CheckboxInput(attrs={'class': 'special', 'placeholder': 'Did you drop out?'}),
        }


class UpdateStudentForm(forms.ModelForm):
    class Meta:
        model = Student
        exclude = ['id', 'dob', 'college']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email id'}),
            'db_folder': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your db_folder name'}),
            'dropped_out': forms.CheckboxInput(attrs={'class': 'special', 'placeholder': 'Did you drop out?'}),
        }
