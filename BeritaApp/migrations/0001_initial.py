# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-10-16 07:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='news_update',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('judul', models.CharField(max_length=100)),
                ('konten', models.CharField(max_length=400)),
            ],
        ),
    ]
