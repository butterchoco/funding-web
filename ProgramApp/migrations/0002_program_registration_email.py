# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-10-15 13:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ProgramApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='program_registration',
            name='email',
            field=models.EmailField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
    ]
