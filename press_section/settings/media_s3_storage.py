import os
from press_section.settings.base import *
from press_section.settings.s3_base import *

# Media files use the default storage, sorl.thumbnail uses this for storage as well
DEFAULT_FILE_STORAGE = 'press_section.storage.DefaultS3BotoStorage'

DEFAULT_S3_PATH = "media"

MEDIA_ROOT = '/%s/' % DEFAULT_S3_PATH
MEDIA_URL = '//%s.s3.amazonaws.com/media/' % AWS_STORAGE_BUCKET_NAME
