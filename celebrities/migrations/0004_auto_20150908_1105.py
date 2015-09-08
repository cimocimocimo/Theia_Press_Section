# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('celebrities', '0003_celebritiespluginmodel_title'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='celebrity',
            options={'ordering': ['order'], 'verbose_name': 'Celebrity', 'verbose_name_plural': 'Celebrities'},
        ),
        migrations.AlterField(
            model_name='celebrity',
            name='order',
            field=models.PositiveIntegerField(default=0, editable=False, db_index=True),
            preserve_default=True,
        ),
    ]
