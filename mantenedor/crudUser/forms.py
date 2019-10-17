from django import forms
from .models import Usuario


class UsuarioForm(forms.ModelForm):
    class Meta:
        model=Usuario
        fields=['rut','nombre','appat','apmat','fecha_nacimiento','email']
        