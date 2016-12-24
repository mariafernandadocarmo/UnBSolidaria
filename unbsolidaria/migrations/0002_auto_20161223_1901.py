# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-12-23 21:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('unbsolidaria', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Organizacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cnpj', models.CharField(blank=True, max_length=45, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Voluntario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cpf', models.CharField(blank=True, max_length=45, null=True)),
                ('gender', models.CharField(blank=True, choices=[('m', 'Masculino'), ('f', 'Feminino')], max_length=1, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='user',
            name='cnpj',
        ),
        migrations.RemoveField(
            model_name='user',
            name='cpf',
        ),
        migrations.RemoveField(
            model_name='user',
            name='gender',
        ),
        migrations.RemoveField(
            model_name='user',
            name='type',
        ),
    ]
