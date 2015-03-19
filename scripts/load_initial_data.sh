#!/bin/sh

# loads the initial data fixtures for my apps.
python manage.py loaddata fixtures/press_contacts.json
python manage.py loaddata fixtures/articles.json
python manage.py loaddata fixtures/events.json
python manage.py loaddata fixtures/celebrities.json
python manage.py loaddata fixtures/cms.json
python manage.py loaddata fixtures/djangocms_style.json
python manage.py loaddata fixtures/djangocms_column.json
python manage.py loaddata fixtures/djangocms_file.json
python manage.py loaddata fixtures/djangocms_flash.json
python manage.py loaddata fixtures/djangocms_googlemap.json
python manage.py loaddata fixtures/djangocms_inherit.json
python manage.py loaddata fixtures/djangocms_link.json
python manage.py loaddata fixtures/djangocms_picture.json
python manage.py loaddata fixtures/djangocms_teaser.json
python manage.py loaddata fixtures/djangocms_video.json
python manage.py loaddata fixtures/djangocms_snippet.json
python manage.py loaddata fixtures/sorl_thumbnail.json
python manage.py loaddata fixtures/gallery.json

