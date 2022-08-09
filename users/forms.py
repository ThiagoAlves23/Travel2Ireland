from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

# BELOW IS ALL THE FORM PULLED FROM MODELS, AND THIS IS RENDERED IN HTML THROUGH VIEWS


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email'
        ]

class SignUpForm(UserCreationForm):

    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2'
        ]

        error_messagens = {
            "username": {
                "required": "Enter the username."
            },
            "first_name": {
                "required": "Enter the first name."
            },
            "last_name": {
                "required": "Enter the last name."
            },
            "email": {
                "required": "Enter the email."
            },
            "password1": {
                "required": "Enter the password."
            },
            "password2": {
                "required": "confirm password."
            },

        }

class ProfileForm(forms.ModelForm):
    DOB = forms.DateField(required=False, help_text='Format date: YYYY-MM-DD', widget=forms.TextInput(
            attrs={
                'class':'form-control','placeholder': 'Date YYYY-MM-DD'
            }
        ))
    city = forms.CharField(required=False, help_text='Your city')
    class Meta:
        model = Profile
        fields = [
            #'age',
            'city',
            'address',
            'contact',
            'DOB',
            'image_profile',
            #'data_cadastro'
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['DOB'].widget = forms.DateInput(format="%d/%m/%Y")
