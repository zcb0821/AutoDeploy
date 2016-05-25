# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-11 06:03
from __future__ import unicode_literals

from django.db import migrations, models
import utilities.djangohelper


class Migration(migrations.Migration):

    dependencies = [
        ('deployment', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cluster',
            name='addrs',
            field=utilities.djangohelper.ListField(null=True),
        ),
        migrations.AddField(
            model_name='cluster',
            name='created',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='cluster',
            name='is_completed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='cluster',
            name='name',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='cluster',
            name='systems',
            field=utilities.djangohelper.ListField(null=True),
        ),
    ]
