# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0008_auto_20141220_2111'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'verbose_name': 'Article', 'verbose_name_plural': 'Articles'},
        ),
        migrations.AddField(
            model_name='article',
            name='excerpt',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='article',
            name='original_publication_date',
            field=models.DateField(default=datetime.date(2014, 12, 21)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='article',
            name='published_date',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 21, 2, 7, 36, 642244)),
            preserve_default=True,
        ),
    ]
