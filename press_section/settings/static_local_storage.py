import os
from press_section.settings.base import *

# Compressor Settings
COMPRESS_ENABLED = False
COMPRESS_OFFLINE = False

COMPRESS_ROOT = STATIC_ROOT = os.path.join(BASE_DIR, 'static')
COMPRESS_URL = STATIC_URL = '/static/'

ADMIN_MEDIA_PREFIX = STATIC_URL + 'admin/'
