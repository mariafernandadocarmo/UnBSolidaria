# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-12-24 04:29
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('unbsolidaria', '0004_user_type_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='type_user',
            new_name='type',
        ),
    ]
