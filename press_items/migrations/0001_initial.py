# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import cms.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0003_auto_20140926_2347'),
    ]

    operations = [
        migrations.CreateModel(
            name='PressItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.TextField(max_length=256)),
                ('organization_name', models.TextField(max_length=256)),
                ('url', models.URLField(max_length=512)),
                ('original_publication_date', models.DateField()),
                ('publication_date', models.DateField()),
                ('content', cms.models.fields.PlaceholderField(slotname=b'press_item_content', editable=False, to='cms.Placeholder', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
