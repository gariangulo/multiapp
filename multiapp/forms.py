# -*- coding: utf-8 -*-
"""
Formularios para la app globales
"""
# Librerias Standard
import datetime
import re

# Librerias Django
from django import forms
from django.forms import ModelForm
from cuenta.models import Persona
from .models import Curso
from dal import autocomplete


class CursosForm (ModelForm):

    class Meta:
        model = Curso
        fields = (
            'nombre_curso',
            'fecha_inicio',
            'total_cupos',
            'tipo_curso',
        )
        labels = {
            'nombre_curso': 'Nombre del Curso',
            'fecha_inicio': 'Fecha de Inicio',
        }
        widgets = {
            'nombre_curso': forms.TextInput(attrs={'class':'form-control'}),
            'total_cupos': forms.NumberInput(attrs={'class':'form-control'}),
            'fecha_inicio': forms.DateField(),
            # 'tipo_curso': autocomplete.ModelSelect2(
            #     url='multiapp:tipo-de-curso',
            #     attrs={
            #         'class': 'form-control select2',
            #         'data-placeholder': 'Tipo de Curso...',
            #     },
            # ),
        }
