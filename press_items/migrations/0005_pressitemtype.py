# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('press_items', '0004_auto_20141217_1414'),
    ]

    operations = [
        migrations.CreateModel(
            name='PressItemType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.TextField(max_length=64)),
                ('slug', models.SlugField(unique=True, max_length=64)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
