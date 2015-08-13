# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0013_auto_20150813_1418'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='address_display',
        ),
        migrations.AlterField(
            model_name='event',
            name='address',
            field=models.TextField(default=b'New York, NY', help_text=b'Used to search Google for the location.'),
            preserve_default=True,
        ),
    ]
