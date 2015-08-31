# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0018_auto_20150828_1434'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='by_appointment_only',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
