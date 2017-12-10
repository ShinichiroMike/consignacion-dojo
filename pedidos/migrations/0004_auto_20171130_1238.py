# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-30 12:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0003_auto_20171123_1656'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pedido',
            old_name='id_pedido',
            new_name='referencia_pedido',
        ),
        migrations.AddField(
            model_name='pedido',
            name='talla',
            field=models.CharField(default='M', max_length=3),
            preserve_default=False,
        ),
    ]
