# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('press_items', '0006_pressitem_item_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pressitemtype',
            name='slug',
            field=models.SlugField(max_length=64, unique=True, null=True, blank=True),
            preserve_default=True,
        ),
    ]
