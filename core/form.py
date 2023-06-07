from django import forms
from django.forms import ModelForm
from .models import Gato, Perro

class GatoForm(ModelForm):
    class Meta:
        model=Gato
        fields="__all__"
        widgets={
            'nombre':forms.TextInput(
                attrs={
                    'placeholder':'Debe ingresar un Nombre',
                    'class':'form-control'
                }
            ),
            'edad':forms.TextInput(
                attrs={
                    'placeholder':'Debe ingresar Edad',
                    'class':'form-control',
                    'type':'number'
                }
            ),
            'comentario':forms.TextInput(
                attrs={
                    'placeholder':'Debe ingresar un Comentario',
                    'class':'form-control'
                }
            ),
            'comuna':forms.Select(
                attrs={
                    'class':'form-control'
                }
            ),
            'genero':forms.Select(
                attrs={
                    'class':'form-control'
                }
            ),
        }
class PerroForm(ModelForm):
    class Meta:
        model=Perro
        fields="__all__"
        widgets={
            'nombre':forms.TextInput(
                attrs={
                    'placeholder':'Debe ingresar un Nombre',
                    'class':'form-control'
                }
            ),
            'edad':forms.TextInput(
                attrs={
                    'placeholder':'Debe ingresar Edad',
                    'class':'form-control',
                    'type':'number'
                }
            ),
            'comentario':forms.TextInput(
                attrs={
                    'placeholder':'Debe ingresar un Comentario',
                    'class':'form-control'
                }
            ),
            'comuna':forms.Select(
                attrs={
                    'class':'form-control'
                }
            ),
            'genero':forms.Select(
                attrs={
                    'class':'form-control'
                }
            ),
        }