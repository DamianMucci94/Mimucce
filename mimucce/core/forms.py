from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
        labels = {
            'username': 'Nombre de usuario',
            'password1': 'Contraseña',
            'password2': 'Confirmar contraseña',
        }
    
    def clean_username(self):
        username = self.cleaned_data.get('username')
        if len(username) > 10:
            raise forms.ValidationError("El nombre de usuario no puede tener más de 10 caracteres.")
        return username