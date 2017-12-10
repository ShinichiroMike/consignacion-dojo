# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-05 13:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('producto', '0001_initial'),
        ('pedidos', '0005_auto_20171205_1353'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pedido',
            name='producto',
        ),
        migrations.AddField(
            model_name='pedido',
            name='producto',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='producto.Producto'),
            preserve_default=False,
        ),
    ]
