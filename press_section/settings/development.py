from press_section.settings.base import *
from press_section.settings.s3_base import *

"""
Local Base Development Settings
"""

DEBUG = True

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

# Shopify settings
SHOPIFY_SHOP_NAME = 'theia2'
SHOPIFY_SHOP_URL = 'https://theia2.myshopify.com/'
SHOPIFY_SHOP_DOMAIN = 'theia.myshopify.com'
SHOPIFY_ADMIN_URL = "https://%s:%s@%s.myshopify.com/admin" % (SHOPIFY_API_KEY, SHOPIFY_PASSWORD, SHOPIFY_SHOP_NAME)

# switch between local and s3 storage
ENABLE_STATIC_LOCAL_STORAGE = True
ENABLE_MEDIA_LOCAL_STORAGE = False

if ENABLE_STATIC_LOCAL_STORAGE:
    from press_section.settings.static_local_storage import *
else:
    from press_section.settings.static_s3_storage import *

if ENABLE_MEDIA_LOCAL_STORAGE:
    from press_section.settings.media_local_storage import *
else:
    from press_section.settings.media_s3_storage import *
