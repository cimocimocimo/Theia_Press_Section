"""
Local Base Development Settings
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

