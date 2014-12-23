# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('celebrities', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='celebrity',
            options={'verbose_name': 'Celebrity', 'verbose_name_plural': 'Celebrities'},
        ),
        migrations.AlterModelOptions(
            name='dress',
            options={'verbose_name': 'Dress', 'verbose_name_plural': 'Dresses'},
        ),
        migrations.AddField(
            model_name='celebrity',
            name='byline',
            field=models.TextField(max_length=128, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='celebrity',
            name='is_featured',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
