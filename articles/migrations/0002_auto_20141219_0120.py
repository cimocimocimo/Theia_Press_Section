# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='item_type',
        ),
        migrations.DeleteModel(
            name='ArticleType',
        ),
        migrations.AlterField(
            model_name='article',
            name='organization_name',
            field=models.TextField(max_length=256, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='article',
            name='original_publication_date',
            field=models.DateField(blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='article',
            name='published_date',
            field=models.DateField(blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='article',
            name='url',
            field=models.URLField(max_length=512, blank=True),
            preserve_default=True,
        ),
    ]
