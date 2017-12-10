# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-30 12:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_tarifa'),
    ]

    operations = [
        migrations.AddField(
            model_name='tarifa',
            name='descripcion',
            field=models.TextField(blank=True, max_length=500),
        ),
        migrations.AddField(
            model_name='tarifa',
            name='nombre',
            field=models.CharField(blank=True, default='', max_length=250),
        ),
        migrations.AlterField(
            model_name='tarifa',
            name='modificador',
            field=models.FloatField(default=0),
        ),
    ]
