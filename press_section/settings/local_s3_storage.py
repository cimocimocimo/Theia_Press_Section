from press_section.settings.base import *
from press_section.settings.local_base import *

"""
Local S3 Storage Settings
"""

# Compressor Settings
COMPRESS_ENABLED = True
COMPRESS_OFFLINE = True

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

# Media files use the default storage, sorl.thumbnail uses this for storage as well
DEFAULT_FILE_STORAGE = 'press_section.storage.DefaultS3BotoStorage'
# static files and compressor for the css/js output
STATICFILES_STORAGE = COMPRESS_STORAGE = 'press_section.storage.StaticS3BotoStorage'

DEFAULT_S3_PATH = "media"
STATIC_S3_PATH = "static"

MEDIA_ROOT = '/%s/' % DEFAULT_S3_PATH
MEDIA_URL = '//%s.s3.amazonaws.com/media/' % AWS_STORAGE_BUCKET_NAME
COMPRESS_ROOT = STATIC_ROOT = os.path.join(BASE_DIR, 'static')
COMPRESS_URL = STATIC_URL = '//%s.s3.amazonaws.com/static/' % AWS_STORAGE_BUCKET_NAME

ADMIN_MEDIA_PREFIX = STATIC_URL + 'admin/'

