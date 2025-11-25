from django import forms

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

        # # Validar longitud mínima
        # if self.cleaned_data['password1'] and self.cleaned_data['password2'] < 5:
        #     self.add_error('password1', 'La contraseña debe tener al menos 5 caracteres')
                