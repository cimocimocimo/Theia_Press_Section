# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0010_auto_20150811_1515'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='address_display',
            field=tinymce.models.HTMLField(default=b'New York, NY', help_text=b'Shown to site visitors.'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='event',
            name='address',
            field=models.CharField(default=b'New York, NY', help_text=b'Used to search Google for the location.', max_length=255),
            preserve_default=True,
        ),
    ]
