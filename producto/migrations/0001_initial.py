# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-15 15:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('color', models.CharField(max_length=100)),
                ('precio_base', models.FloatField()),
                ('deleted', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Talla',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=3)),
                ('incremento', models.FloatField()),
                ('deleted', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Tallaje',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, unique=True)),
                ('deleted', models.BooleanField(default=False)),
            ],
        ),
        migrations.AddField(
            model_name='talla',
            name='tallaje',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='producto.Tallaje'),
        ),
        migrations.AddField(
            model_name='producto',
            name='tallaje',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='producto.Tallaje'),
        ),
    ]
