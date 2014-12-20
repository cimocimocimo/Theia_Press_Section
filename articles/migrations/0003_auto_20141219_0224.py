# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_auto_20141219_0120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='organization_name',
            field=models.TextField(default=b'', max_length=256, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='article',
            name='original_publication_date',
            field=models.DateField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='article',
            name='published_date',
            field=models.DateField(default=datetime.date(2014, 12, 19)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='article',
            name='url',
            field=models.URLField(default=b'', max_length=512, blank=True),
            preserve_default=True,
        ),
    ]
