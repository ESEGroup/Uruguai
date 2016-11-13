# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-12 23:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('simte', '0003_auto_20161112_2311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inspection',
            name='equipment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='simte.Equipment', verbose_name='Equipment'),
        ),
        migrations.AlterField(
            model_name='piece',
            name='equipment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='simte.Equipment', verbose_name='Equipment'),
        ),
    ]