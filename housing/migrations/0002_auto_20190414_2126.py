# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-04-14 21:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('housing', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='lat',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='post',
            name='lng',
            field=models.FloatField(default=0.0),
        ),
    ]
