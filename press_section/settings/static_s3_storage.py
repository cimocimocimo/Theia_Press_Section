import os
from press_section.settings.base import *
from press_section.settings.s3_base import *

"""
base settings for the storing static files on s3
"""

# Compressor Settings
COMPRESS_ENABLED = True
COMPRESS_OFFLINE = False

# static files and compressor for the css/js output
STATICFILES_STORAGE = COMPRESS_STORAGE = 'press_section.storage.StaticS3BotoStorage'
STATIC_S3_PATH = "static"

COMPRESS_ROOT = STATIC_ROOT = os.path.join(BASE_DIR, 'static')
COMPRESS_URL = STATIC_URL = '//%s.s3.amazonaws.com/static/' % AWS_STORAGE_BUCKET_NAME

ADMIN_MEDIA_PREFIX = STATIC_URL + 'admin/'
