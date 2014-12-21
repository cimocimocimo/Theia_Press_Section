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
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.TextField(max_length=256)),
                ('slug', models.SlugField(unique=True, max_length=64)),
                ('event_date', models.DateField(default=datetime.date(2014, 12, 21))),
                ('published_date', models.DateTimeField(default=datetime.datetime(2014, 12, 21, 16, 10, 45, 636423))),
                ('content', cms.models.fields.PlaceholderField(slotname=b'event_content', editable=False, to='cms.Placeholder', null=True)),
                ('video_still', filer.fields.image.FilerImageField(blank=True, to='filer.Image', null=True)),
            ],
            options={
                'verbose_name': 'Event',
                'verbose_name_plural': 'Events',
            },
            bases=(models.Model,),
        ),
    ]
