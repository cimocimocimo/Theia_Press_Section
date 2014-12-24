# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import filer.fields.image
import datetime
import cms.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0003_auto_20140926_2347'),
        ('filer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField(unique=True, max_length=64)),
                ('organization_name', models.CharField(max_length=255, null=True, blank=True)),
                ('url', models.URLField(max_length=512, null=True, blank=True)),
                ('original_publication_date', models.DateField(default=datetime.date.today)),
                ('published_date', models.DateTimeField(default=datetime.datetime.now)),
                ('excerpt', models.TextField(null=True, blank=True)),
                ('content', cms.models.fields.PlaceholderField(slotname=b'press_item_content', editable=False, to='cms.Placeholder', null=True)),
                ('screenshot', filer.fields.image.FilerImageField(blank=True, to='filer.Image', null=True)),
            ],
            options={
                'verbose_name': 'Article',
                'verbose_name_plural': 'Articles',
            },
            bases=(models.Model,),
        ),
    ]
