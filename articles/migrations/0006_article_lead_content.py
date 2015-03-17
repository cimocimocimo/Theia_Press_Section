# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0005_article_screenshot_2'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='lead_content',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
