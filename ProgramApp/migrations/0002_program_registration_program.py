# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-10-19 12:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProgramApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='program_registration',
            name='program',
            field=models.ManyToManyField(to='ProgramApp.program_update'),
        ),
    ]
