# Generated by Django 2.0.13 on 2019-04-28 23:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('housing', '0009_auto_20190428_1921'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=models.CharField(blank=True, max_length=300),
        ),
    ]
