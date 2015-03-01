#!/bin/sh

# loads the initial data fixtures for my apps.
python manage.py loaddata celebrities/data_initial.json
