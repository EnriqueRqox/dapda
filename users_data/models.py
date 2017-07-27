# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.validators import RegexValidator
from django.db import models


TOURIMS = 'TUR'
ALL_ROAD = 'ALL'
COMERCIAL = 'COM'

VEHICLE_TYPES = (
    (TOURIMS, 'Turismo'),
    (ALL_ROAD, 'Todo terreno'),
    (COMERCIAL, 'Comercial')
)


CORSA = 'COR'
ASTRA = 'AST'
MOKKA = 'MOK'
CROSSLAND = 'CRO'

VEHICLES = (
    (CORSA, 'Corsa'),
    (ASTRA, 'Astra'),
    (MOKKA, 'Mokka'),
    (CROSSLAND, 'Crossland')
)


MORNING = 'MON'
AFTERNOON = 'AFT'
NIGHT = 'NIG'

CALL_PREFERENCES = (
    (MORNING, 'Mañana'),
    (AFTERNOON, 'Tarde'),
    (NIGHT, 'Noche')
)


class UserData(models.Model):

    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    phone = models.CharField(
        max_length=9,
        validators=[
            RegexValidator(
                regex='^[9|6|7][0-9]{8}$',
                message='El teléfono debe empezar por 6, 7 ó 9, y estar compuesto por 9 dígitos',
                code='invalid_phone'
            ),
        ]
    )
    email = models.EmailField()
    vehicle_type = models.CharField(max_length=3, choices=VEHICLE_TYPES)
    vehicle = models.CharField(max_length=3, choices=VEHICLES)
    call_preference = models.CharField(max_length=3, choices=CALL_PREFERENCES)

    def __unicode__(self):  # 0 param method
        return self.first_name
