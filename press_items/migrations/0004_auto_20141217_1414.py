# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('press_items', '0003_pressitem_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pressitem',
            name='slug',
            field=models.SlugField(unique=True, max_length=256),
            preserve_default=True,
        ),
    ]
