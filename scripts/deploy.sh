#!/bin/sh

# dump data from django
python manage.py dumpdata --natural-foreign press_contacts > fixtures/press_contacts.json
python manage.py dumpdata --natural-foreign articles > fixtures/articles.json
python manage.py dumpdata --natural-foreign events > fixtures/events.json
python manage.py dumpdata --natural-foreign celebrities > fixtures/celebrities.json
python manage.py dumpdata --natural-foreign cms > fixtures/cms.json
python manage.py dumpdata --natural-foreign djangocms_style > fixtures/djangocms_style.json
python manage.py dumpdata --natural-foreign djangocms_column > fixtures/djangocms_column.json
python manage.py dumpdata --natural-foreign djangocms_file > fixtures/djangocms_file.json
python manage.py dumpdata --natural-foreign djangocms_flash > fixtures/djangocms_flash.json
python manage.py dumpdata --natural-foreign djangocms_googlemap > fixtures/djangocms_googlemap.json
python manage.py dumpdata --natural-foreign djangocms_inherit > fixtures/djangocms_inherit.json
python manage.py dumpdata --natural-foreign djangocms_link > fixtures/djangocms_link.json
python manage.py dumpdata --natural-foreign djangocms_picture > fixtures/djangocms_picture.json
python manage.py dumpdata --natural-foreign djangocms_teaser > fixtures/djangocms_teaser.json
python manage.py dumpdata --natural-foreign djangocms_video > fixtures/djangocms_video.json
python manage.py dumpdata --natural-foreign djangocms_snippet > fixtures/djangocms_snippet.json
python manage.py dumpdata --natural-foreign thumbnail > fixtures/sorl_thumbnail.json
python manage.py dumpdata --natural-foreign gallery > fixtures/gallery.json
