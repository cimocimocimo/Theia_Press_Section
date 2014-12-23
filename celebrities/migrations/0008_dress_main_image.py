# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import filer.fields.image


class Migration(migrations.Migration):

    dependencies = [
        ('filer', '0001_initial'),
        ('celebrities', '0007_auto_20141222_0206'),
    ]

    operations = [
        migrations.AddField(
            model_name='dress',
            name='main_image',
            field=filer.fields.image.FilerImageField(default=0, to='filer.Image'),
            preserve_default=False,
        ),
    ]
