# Generated by Django 2.0.13 on 2019-04-04 00:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0028_auto_20190403_1955'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='profile_pic',
            field=models.CharField(default='', max_length=400),
        ),
    ]
