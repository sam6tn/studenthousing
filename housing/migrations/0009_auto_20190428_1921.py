# Generated by Django 2.0.13 on 2019-04-28 23:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('housing', '0008_auto_20190427_1638'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=models.TextField(blank=True, max_length=300),
        ),
    ]
