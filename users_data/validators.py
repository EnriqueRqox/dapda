# -*- coding: utf-8 -*-
from django.core.exceptions import ValidationError


def phone_validator(value):
    '''
    it validates whether the value starts with a 6, 7 or 9 and contains 9 digits
    '''

