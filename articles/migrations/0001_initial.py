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
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.TextField(max_length=256)),
                ('slug', models.SlugField(unique=True, max_length=64)),
                ('organization_name', models.TextField(max_length=256)),
                ('url', models.URLField(max_length=512)),
                ('original_publication_date', models.DateField()),
                ('published_date', models.DateField()),
                ('content', cms.models.fields.PlaceholderField(slotname=b'press_item_content', editable=False, to='cms.Placeholder', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ArticleType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.TextField(max_length=64)),
                ('slug', models.SlugField(unique=True, max_length=64)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='article',
            name='item_type',
            field=models.ForeignKey(to='articles.ArticleType'),
            preserve_default=True,
        ),
    ]
