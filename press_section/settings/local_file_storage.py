from press_section.settings.base import *
from press_section.settings.local_base import *

"""
Local Filestorage Development Settings
"""

# Compressor Settings
COMPRESS_ENABLED = False
COMPRESS_OFFLINE = False

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
COMPRESS_ROOT = STATIC_ROOT = os.path.join(BASE_DIR, 'static')
COMPRESS_URL = STATIC_URL = '/static/'

ADMIN_MEDIA_PREFIX = STATIC_URL + 'admin/'

