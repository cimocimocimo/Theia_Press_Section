# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import sorl.thumbnail.fields
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
                ('order', models.PositiveIntegerField(editable=False, db_index=True)),
                ('name', models.CharField(max_length=255)),
                ('byline', models.CharField(max_length=128, null=True, blank=True)),
                ('main_image', sorl.thumbnail.fields.ImageField(null=True, upload_to=b'', blank=True)),
                ('slug', models.SlugField(unique=True, max_length=255)),
                ('content', cms.models.fields.PlaceholderField(slotname=b'celebrity_content', editable=False, to='cms.Placeholder', null=True)),
            ],
            options={
                'ordering': ('order',),
                'abstract': False,
                'verbose_name': 'Celebrity',
                'verbose_name_plural': 'Celebrities',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Dress',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('order', models.PositiveIntegerField(editable=False, db_index=True)),
                ('title', models.CharField(max_length=255)),
                ('main_image', sorl.thumbnail.fields.ImageField(null=True, upload_to=b'', blank=True)),
                ('slug', models.SlugField(unique=True, max_length=255)),
                ('celebrity', models.ForeignKey(to='celebrities.Celebrity')),
                ('content', cms.models.fields.PlaceholderField(slotname=b'celebrity_content', editable=False, to='cms.Placeholder', null=True)),
            ],
            options={
                'ordering': ('order',),
                'abstract': False,
                'verbose_name': 'Dress',
                'verbose_name_plural': 'Dresses',
            },
            bases=(models.Model,),
        ),
    ]
