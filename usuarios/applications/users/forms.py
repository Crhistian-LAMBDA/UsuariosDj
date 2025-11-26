from django import forms
from django.contrib.auth import authenticate
from .models import User

class UserRegisterForm(forms.ModelForm):   

    password1 = forms.CharField(
        label='Contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Contraseña'
            }
        )

    )
    password2 = forms.CharField(
        label='Contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Repetir Contraseña'
            }
        )

    )

    class Meta:
        """Meta definition form"""

        model = User
        fields = (
            'username',
            'email',
            'nombres',
            'apellidos',
            'genero',

        )

    #funcion de validacion password
    def clean_password2(self):

        if self.cleaned_data['password1'] != self.cleaned_data['password2']:
            self.add_error('password2', 'Error contraseñas no coinciden')

class LoginForm(forms.Form): 

    username = forms.CharField(
        label='username',
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'username',
                'style': '{margin: 10px}',
            }
        )
    )

    password = forms.CharField(
        label='Contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Contraseña'
            }
        )
    )

    #validacion
    def clean(self):
        cleaned_data = super(LoginForm, self).clean()
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']
        if not authenticate(username=username, password=password):
            raise forms.ValidationError('Los datos del usuario no son correctos')
        
        return self.cleaned_data




class UpdatePasswordForm (forms.Form):
        
    password1 = forms.CharField(
        label='Contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Contraseña Actual'
            }
        )
    )
    password2 = forms.CharField(
        label='Contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Contraseña Nueva'
            }
        )
    )

   #validacion
    # def clean(self):
    #     cleaned_data = super(UpdatePasswordForm, self).clean()
    #     password1 = self.cleaned_data['password1']
    #     password2 = self.cleaned_data['password2']
    #     if not authenticate(password1=password1, password2=password2):
    #         raise forms.ValidationError('Los datos del usuario no son correctos')
        
    #     return self.cleaned_data