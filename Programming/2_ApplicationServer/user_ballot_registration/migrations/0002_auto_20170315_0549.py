# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-15 05:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_ballot_registration', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requestsigniture',
            name='token',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='requestsigniture',
            name='token_signed',
            field=models.CharField(max_length=1000),
        ),
    ]
