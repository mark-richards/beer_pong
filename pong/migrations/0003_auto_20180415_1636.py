# Generated by Django 2.0.3 on 2018-04-15 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pong', '0002_auto_20180410_2132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='away_cups_remaining',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='match',
            name='home_cups_remaining',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
