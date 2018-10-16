# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-10-16 06:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user_registration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=255)),
                ('tanggal_lahir', models.DateField()),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
    ]
