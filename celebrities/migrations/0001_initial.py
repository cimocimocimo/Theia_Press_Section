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
            name='Celebrity',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.TextField(max_length=256)),
                ('slug', models.SlugField(unique=True, max_length=256)),
                ('content', cms.models.fields.PlaceholderField(slotname=b'celebrity_content', editable=False, to='cms.Placeholder', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Dress',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.TextField(max_length=256)),
                ('slug', models.SlugField(unique=True, max_length=256)),
                ('celebrity', models.ForeignKey(to='celebrities.Celebrity')),
                ('content', cms.models.fields.PlaceholderField(slotname=b'celebrity_content', editable=False, to='cms.Placeholder', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
