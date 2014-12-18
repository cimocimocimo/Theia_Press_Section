# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('press_items', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pressitem',
            old_name='publication_date',
            new_name='published_date',
        ),
    ]
