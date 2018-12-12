from django import forms


class SignUpForm(forms.Form):

    first_name = forms.CharField(
        max_length=75,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your First Name'}),
        label='Your First Name:'
    )

    last_name = forms.CharField(
        max_length=75,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your Last Name'}),
        label='Your Last Name:'
    )

    username = forms.CharField(
        max_length=75,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your Username'}),
        label='Your Username:'
    )

    password = forms.CharField(
        max_length=25,
        required=True,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter your Password'}),
        label='Enter Password:'
    )


class LoginForm(forms.Form):

    username = forms.CharField(
        max_length=75,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your Username'}),
        label='Your Username:'
    )

    password = forms.CharField(
        max_length=25,
        required=True,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter your Password'}),
        label='Enter Password:'
    )
