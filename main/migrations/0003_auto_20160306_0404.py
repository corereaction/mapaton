# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-06 10:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20160305_2247'),
    ]

    operations = [
        migrations.AddField(
            model_name='ruta',
            name='primerPunto',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='ruta',
            name='ultimoPunto',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
