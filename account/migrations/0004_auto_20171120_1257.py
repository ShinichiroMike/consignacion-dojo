# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-20 12:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_auto_20171120_1253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='codigo_postal',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='direccion',
            field=models.CharField(blank=True, default='', max_length=250),
        ),
        migrations.AlterField(
            model_name='profile',
            name='forma_de_pago',
            field=models.CharField(blank=True, default='', max_length=250),
        ),
        migrations.AlterField(
            model_name='profile',
            name='localidad',
            field=models.CharField(blank=True, default='', max_length=250),
        ),
        migrations.AlterField(
            model_name='profile',
            name='provincia',
            field=models.CharField(blank=True, default='', max_length=250),
        ),
        migrations.AlterField(
            model_name='profile',
            name='telefono',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='profile',
            name='telefono_movil',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
