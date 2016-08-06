from press_section.settings.base import *
from press_section.settings.s3_base import *
from press_section.settings.static_s3_storage import *
from press_section.settings.media_s3_storage import *

"""
Production Settings
"""

TEMPLATE_DEBUG = DEBUG = False

ALLOWED_HOSTS = ['press.theiacouture.com', 'press-section-dev.elasticbeanstalk.com']

# Production Shopify settings
SHOPIFY_SHOP_NAME = 'theia'
SHOPIFY_SHOP_URL = 'https://theiacouture.com/'
SHOPIFY_ADMIN_URL = "https://%s:%s@%s.myshopify.com/admin" % (SHOPIFY_API_KEY, SHOPIFY_PASSWORD, SHOPIFY_SHOP_NAME)

# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases
if 'RDS_DB_NAME' in os.environ:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': os.environ['RDS_DB_NAME'],
            'USER': os.environ['RDS_USERNAME'],
            'PASSWORD': os.environ['RDS_PASSWORD'],
            'HOST': os.environ['RDS_HOSTNAME'],
            'PORT': os.environ['RDS_PORT'],
        }
    }


