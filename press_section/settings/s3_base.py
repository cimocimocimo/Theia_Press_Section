import os
from press_section.settings.base import *

"""
Base settings for s3 based storages.
"""

# Django Storages
AWS_ACCESS_KEY_ID = os.environ['AWS_ACCESS_KEY_ID']
AWS_SECRET_KEY = os.environ['AWS_SECRET_KEY']
AWS_STORAGE_BUCKET_NAME = 'theia-press-section-assets'
S3_URL = 'https://%s.s3.amazonaws.com/' % AWS_STORAGE_BUCKET_NAME

# Used to make sure that only changed files are uploaded with collectstatic
AWS_PRELOAD_METADATA = True

# remove the auth string from the generated static file urls
# this setting was not working last I checked - AC 2015-01-25
# needed to overridethis in a subclass
AWS_QUERYSTRING_AUTH = False
AWS_S3_SECURE_URLS = False
