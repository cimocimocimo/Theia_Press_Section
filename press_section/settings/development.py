from press_section.settings.base import *

"""
Local Development Settings
"""

TEMPLATE_DEBUG = DEBUG = True

ALLOWED_HOSTS = ['*']

DATABASES = {
 'default': {
  'ENGINE': 'django.db.backends.mysql',
  'NAME': 'theia_press_section',
  'USER': 'root',
  'PASSWORD': '',
  'HOST': 'localhost',
  'PORT': '3306',
 }
}

# Compressor Settings
COMPRESS_ENABLED = False
COMPRESS_OFFLINE = False

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
COMPRESS_ROOT = STATIC_ROOT = os.path.join(BASE_DIR, 'static')
COMPRESS_URL = STATIC_URL = '/static/'

ADMIN_MEDIA_PREFIX = STATIC_URL + 'admin/'

