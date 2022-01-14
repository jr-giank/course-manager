#Importaciones de Django
from typing import Text
from django.contrib.auth.models import User
from django.db.models.fields import Field
from Home.models import Cursos
from django import forms
from django.core.exceptions import ValidationError

class SignUpForm(forms.Form):

    first_name = forms.CharField(
        max_length=25,
        required=True,
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
        required=True,
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
        required=True,
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
        required=True,
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
        required=True,
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
        required=True,
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

        
class LoginForm(forms.Form):

    username = forms.CharField(
        max_length=35,
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'required': True
            }
        )
    )

    password = forms.CharField(
        max_length=20,
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'required': True
            }
        )
    )

class AgregarCursosForm(forms.Form):

    creditos = forms.IntegerField(
        label=False,
        required=True,
        max_value=5,
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control text-center',
                'placeholder': 'Creditos',
            }
        )
    )

    nombre_asignatura = forms.CharField(
        label=False,
        required=True,
        max_length=45,
        widget= forms.TextInput(
            attrs={
                'class': 'form-control text-center',
                'placeholder': 'Asignatura'
            }
        )
    )

    costo = forms.DecimalField(
        label=False,
        required=True,
        max_digits=6,
        widget=forms.NumberInput(
            attrs={ 
                'class': 'form-control text-center',
                'placeholder': 'Costo'
            }
        )
    )

    def clean(self):

        data = super().clean()

        return data

    def save(self):

        data = self.cleaned_data

        asignatura = Cursos.objects.create(**data)

class ModificarForm(forms.Form):

    datos = Cursos.objects.filter(nombre_asignatura='Programación I')

    """creditos = forms.IntegerField(
        label=False,
        required=True,
        Field= datos, 
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control text-center',
                'value': 'Hola'
            }
            
        )
    )"""
