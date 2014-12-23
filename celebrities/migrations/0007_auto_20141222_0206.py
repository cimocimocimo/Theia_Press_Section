# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('celebrities', '0006_auto_20141222_0129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='celebrity',
            name='byline',
            field=models.CharField(max_length=128, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='celebrity',
            name='name',
            field=models.CharField(max_length=256),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='dress',
            name='title',
            field=models.CharField(max_length=256),
            preserve_default=True,
        ),
    ]
