# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_latestarticlespluginmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='latestarticlespluginmodel',
            name='number_to_show',
            field=models.PositiveSmallIntegerField(default=4),
            preserve_default=True,
        ),
    ]
