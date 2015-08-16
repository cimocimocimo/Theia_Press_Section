# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0015_eventconfig'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='content',
            field=tinymce.models.HTMLField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
