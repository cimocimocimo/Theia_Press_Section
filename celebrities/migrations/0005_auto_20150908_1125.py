# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('celebrities', '0004_auto_20150908_1105'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='dress',
            options={'verbose_name': 'Dress', 'verbose_name_plural': 'Dresses'},
        ),
        migrations.RemoveField(
            model_name='dress',
            name='order',
        ),
    ]
