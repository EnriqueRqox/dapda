# -*- coding: utf-8 -*-
from django import forms
from django.core.exceptions import ValidationError

from users_data.models import UserData


class UserDataForm(forms.ModelForm):
    """
    Formulario para el modelo User Data
    """
    class Meta:
        model = UserData
        fields = '__all__'
        labels = {
            'first_name': 'Nombre',
            'last_name': 'Apellidos',
            'phone': 'Teléfono',
            'email': 'Correo electrónico',
            'vehicle_type': 'Tipo de vehículo',
            'vehicle': 'Vehículo',
            'call_preference': 'Preferencia de llamada'
        }

    # def clean_phone(self):
    #     phone = self.cleaned_data.get('phone', False)

    # def clean(self):
    #
    #
    #
    #     return super(forms.ModelForm, self).clean(self)
