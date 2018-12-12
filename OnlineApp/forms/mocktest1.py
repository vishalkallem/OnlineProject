from django import forms
from OnlineApp.models import *


class MockTestForm(forms.ModelForm):
    class Meta:
        model = MockTest1
        exclude = ['id', 'total', 'student']
        widgets = {
            'problem1': forms.NumberInput(attrs={'class': 'form-control',
                                                 'placeholder': 'Enter your score in problem 1'}),
            'problem2': forms.NumberInput(attrs={'class': 'form-control',
                                                 'placeholder': 'Enter your score in problem 2'}),
            'problem3': forms.NumberInput(attrs={'class': 'form-control',
                                                 'placeholder': 'Enter your score in problem 3'}),
            'problem4': forms.NumberInput(attrs={'class': 'form-control',
                                                 'placeholder': 'Enter your score in problem 4'}),
        }


class UpdateMockTestForm(forms.ModelForm):
    class Meta:
        model = MockTest1
        exclude = ['id', 'total', 'student']
        widgets = {
            'problem1': forms.NumberInput(attrs={'class': 'form-control',
                                                 'placeholder': 'Enter your score in problem 1'}),
            'problem2': forms.NumberInput(attrs={'class': 'form-control',
                                                 'placeholder': 'Enter your score in problem 2'}),
            'problem3': forms.NumberInput(attrs={'class': 'form-control',
                                                 'placeholder': 'Enter your score in problem 3'}),
            'problem4': forms.NumberInput(attrs={'class': 'form-control',
                                                 'placeholder': 'Enter your score in problem 4'}),
        }
