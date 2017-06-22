import os

"""
Django settings for press_section project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

ADMINS = (('Aaron Cimolini', 'aaron@cimolini.com'),)

# Amazon SES settings for sending emails
# only authorized to send to/from aaron@cimolini.com
EMAIL_HOST = 'email-smtp.us-east-1.amazonaws.com'
EMAIL_HOST_PASSWORD = 'ArRShrMAXfhjkq0Y5Oj7Jt02MdogInJG26D+eKEscPbY'
EMAIL_HOST_USER = 'AKIAJBTRFE5YWGEZPWVQ'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
SERVER_EMAIL = 'aaron@cimolini.com' # this is the email that is authorized to send from/to through Amazon SES.

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
gettext = lambda s: s
# ugly but works.
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ['DJANGO_SECRET_KEY']

# Application definition
ROOT_URLCONF = 'press_section.urls'
WSGI_APPLICATION = 'press_section.wsgi.application'

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/
LANGUAGE_CODE = 'en'
TIME_ZONE = 'US/Eastern'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'press_section', 'static'),
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    # other finders..
    'compressor.finders.CompressorFinder',
)


# if using scss precompiler use the compress.sh script for the compress command on Elastic Beanstalk
COMPRESS_PRECOMPILERS = (
    # ('text/scss', 'sass --scss {infile} {outfile}'),
    # ('text/scss', 'press_section.helpers.ScssFilter'),
)

# fixes an issue with absolute urls
COMPRESS_CSS_FILTERS = [
    'press_section.compressor_filters.CustomCssAbsoluteFilter'
]


SITE_ID = 1

MIDDLEWARE_CLASSES = (
    'corsheaders.middleware.CorsMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.contrib.admindocs.middleware.XViewMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'cms.middleware.language.LanguageCookieMiddleware'
)

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'APP_DIRS': True,
        'DIRS': [
            os.path.join(BASE_DIR, 'press_section', 'templates'),
        ],
        'OPTIONS': {
            'context_processors':
            (
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.i18n',
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.template.context_processors.media',
                'django.template.context_processors.csrf',
                'django.template.context_processors.tz',
                'django.template.context_processors.static',
                'sekizai.context_processors.sekizai',
                'cms.context_processors.cms_settings',
                'press_section.context_processors.appname',
                'press_section.context_processors.site_domain',
                'press_section.context_processors.shopify_settings',
            )
        }
    },
]

INSTALLED_APPS = (

    # Theia apps
    'pagination',
    'cms_extra_tags',
    'press_contacts',
    'articles',
    'events',
    'celebrities',
    'press_section',
    'gallery',
    'videos',
    # 'product_import',

    'djangocms_admin_style',
    'djangocms_text_ckeditor',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.admin',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'django.contrib.staticfiles',
    'django.contrib.messages',
    'cms',
    'treebeard',
    'menus',
    'sekizai',
    'djangocms_style',
    'djangocms_column',
    'djangocms_file',
    'djangocms_flash',
    'djangocms_googlemap',
    'djangocms_inherit',
    'djangocms_link',
    'djangocms_picture',
    'djangocms_teaser',
    'djangocms_video',
    'djangocms_snippet', # **TODO** possible security risk, add custom plugin for adding blocks of html
    'reversion',
    'compressor',
    'ordered_model',
    'adminsortable',
    'storages',
    'corsheaders',
    'sorl.thumbnail',
    'debug_toolbar',
    'location_field',
    'solo',
    'tinymce',
    'taggit',
    'taggit_labels',
    'embed_video',
)

LANGUAGES = (
    ## Customize this
    ('en', gettext('en')),
    ('fr', gettext('fr')),
)

CMS_LANGUAGES = {
    ## Customize this
    'default': {
        'public': True,
        'hide_untranslated': False,
        'redirect_on_fallback': True,
    },
    1: [
        {
            'public': True,
            'code': 'en',
            'hide_untranslated': False,
            'name': gettext('en'),
            'redirect_on_fallback': True,
        },
        {
            'public': True,
            'code': 'fr',
            'hide_untranslated': False,
            'name': gettext('fr'),
            'redirect_on_fallback': True,
        },
    ],
}

CMS_TEMPLATES = (
    ## Customize this
    ('page.tmpl.html', 'Page'),
    ('feature.tmpl.html', 'Page with Feature')
)

CMS_PERMISSION = True

CMS_PLACEHOLDER_CONF = {}

CORS_ORIGIN_ALLOW_ALL = True

TINYMCE_DEFAULT_CONFIG = {
    'theme': 'advanced',
    'resize': 'both',
    'width': '100%',
    'plugins': 'autoresize',
}

# Base Shopify settings
# SHOPIFY_API_KEY = os.environ['SHOPIFY_API_KEY']
# SHOPIFY_PASSWORD = os.environ['SHOPIFY_PASSWORD']

# Dropbox Settings
# DROPBOX_TOKEN = os.environ['DROPBOX_TOKEN']
