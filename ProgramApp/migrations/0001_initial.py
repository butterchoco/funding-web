# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-10-18 04:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='program_registration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=100)),
                ('jumlah_uang', models.IntegerField()),
                ('tampilkan', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='program_update',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('judul', models.CharField(max_length=50)),
                ('konten', models.TextField(max_length=500)),
                ('image', models.CharField(max_length=200)),
            ],
        ),
    ]
