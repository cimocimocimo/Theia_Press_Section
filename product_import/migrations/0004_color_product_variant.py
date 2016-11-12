# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-11-12 21:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_import', '0003_auto_20161110_2213'),
    ]

    operations = [
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('code', models.CharField(max_length=8)),
                ('display_name', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('season', models.CharField(max_length=128)),
                ('style_number', models.CharField(max_length=64)),
                ('name', models.CharField(max_length=256)),
                ('division', models.CharField(max_length=64)),
                ('wholesale_usd', models.PositiveIntegerField()),
                ('retail_usd', models.PositiveIntegerField()),
                ('category', models.CharField(max_length=64)),
                ('available_start', models.DateField()),
                ('available_end', models.DateField()),
                ('description', models.TextField()),
                ('archived', models.BooleanField()),
                ('brand_id', models.CharField(max_length=64)),
                ('wholesale_cad', models.PositiveIntegerField()),
                ('retail_cad', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Variant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]
