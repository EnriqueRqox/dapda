# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-07-27 14:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users_data', '0002_auto_20170727_1418'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdata',
            name='vehicle',
            field=models.CharField(choices=[('COR', 'Corsa'), ('AST', 'Astra'), ('MOK', 'Mokka'), ('CRO', 'Crossland')], max_length=3),
        ),
    ]
