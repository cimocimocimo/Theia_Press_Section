#!/bin/sh

# prepare the deployments to the server

# dump data from django

python manage.py dumpdata press_contacts > fixtures/press_contacts.json
python manage.py dumpdata articles > fixtures/articles.json
python manage.py dumpdata events > fixtures/events.json
python manage.py dumpdata celebrities > fixtures/celebrities.json
python manage.py dumpdata press_section > fixtures/press_section.json
python manage.py dumpdata cms > fixtures/cms.json
python manage.py dumpdata menus > fixtures/menus.json
python manage.py dumpdata djangocms_style > fixtures/djangocms_style.json
python manage.py dumpdata djangocms_column > fixtures/djangocms_column.json
python manage.py dumpdata djangocms_file > fixtures/djangocms_file.json
python manage.py dumpdata djangocms_flash > fixtures/djangocms_flash.json
python manage.py dumpdata djangocms_googlemap > fixtures/djangocms_googlemap.json
python manage.py dumpdata djangocms_inherit > fixtures/djangocms_inherit.json
python manage.py dumpdata djangocms_link > fixtures/djangocms_link.json
python manage.py dumpdata djangocms_picture > fixtures/djangocms_picture.json
python manage.py dumpdata djangocms_teaser > fixtures/djangocms_teaser.json
python manage.py dumpdata djangocms_video > fixtures/djangocms_video.json
python manage.py dumpdata djangocms_snippet > fixtures/djangocms_snippet.json
python manage.py dumpdata reversion > fixtures/reversion.json
python manage.py dumpdata compressor > fixtures/compressor.json
python manage.py dumpdata sorl.thumbnail > fixtures/sorl_thumbnail.json
