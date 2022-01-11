#Importaciones de Django
from django.contrib.auth.models import User
from django import forms
from django.core.exceptions import ValidationError

class SignUpForm(forms.Form):

    first_name = forms.CharField(
        max_length=25,
        widget=forms.TextInput(
            attrs={
                'class':"form-control", 
                'name':"First Name", 
                'required':"true"
            }
        )
    ) 

    last_name = forms.CharField(
        max_length=25,
        widget=forms.TextInput(
            attrs={
                'class':"form-control", 
                'name':"Last Name", 
                'required':"true"
            }
        )
    ) 

    username = forms.CharField(
        max_length=25,
        widget=forms.TextInput(
            attrs={
                'class':"form-control", 
                'name':"Username", 
                'required':"true"
            }
        )
    ) 

    email = forms.EmailField(
        max_length=70,
        widget=forms.TextInput(
            attrs={
                'class':"form-control", 
                'name':"Email", 
                'required':"true"
            }
        )
    ) 

    password = forms.CharField(
        max_length=25,
        widget=forms.PasswordInput(
            attrs={
                'class':"form-control", 
                'name':"Password", 
                'required':"true"
            }
        )
    ) 

    password_confirmation = forms.CharField(
        max_length=25,
        widget=forms.PasswordInput(
            attrs={
                'class':"form-control", 
                'name':"Password Confirmation", 
                'required':"true"
            }
        )
    ) 

    def clean_username(self):

        username = self.cleaned_data['username']
        username_taken = User.objects.filter(username=username).exists()

        if username_taken == True:
            raise ValidationError('Username is already taken')

        return username

    def clean(self):
        data = super().clean()

        password = data['password']
        password_confirmation = data['password_confirmation']

        if password != password_confirmation:
            raise ValidationError('Password does not match')

        return data

    def save(self):
        data = self.cleaned_data

        data.pop('password_confirmation')

        user = User.objects.create_user(**data)

        
