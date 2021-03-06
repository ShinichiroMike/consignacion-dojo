# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-20 13:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_auto_20171120_1257'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='deuda_cliente',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='profile',
            name='estado_cliente',
            field=models.CharField(blank=True, default='activo', max_length=250),
        ),
        migrations.AlterField(
            model_name='profile',
            name='forma_de_pago',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='numero_de_cuenta',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='telefono',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='telefono_movil',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
