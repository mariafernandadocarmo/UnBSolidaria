# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-12-24 04:57
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('unbsolidaria', '0005_auto_20161224_0229'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='organizacao',
            name='user_fk',
        ),
        migrations.RemoveField(
            model_name='voluntario',
            name='user_fk',
        ),
        migrations.AddField(
            model_name='organizacao',
            name='organizacao_fk',
            field=models.ForeignKey(default=-1, on_delete=django.db.models.deletion.CASCADE, related_name='organizacao_fk', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='voluntario',
            name='voluntario_fk',
            field=models.ForeignKey(default=-1, on_delete=django.db.models.deletion.CASCADE, related_name='voluntario_fk', to=settings.AUTH_USER_MODEL),
        ),
    ]
