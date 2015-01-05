import os
import re
import posixpath

from compressor.cache import get_hashed_mtime, get_hashed_content
from compressor.conf import settings
from compressor.filters import FilterBase, FilterError
from compressor.filters.css_default import CssAbsoluteFilter
from compressor.utils import staticfiles

URL_PATTERN = re.compile(r'url\(([^\)]+)\)')
SRC_PATTERN = re.compile(r'src=([\'"])(.+?)\1')
SCHEMES = ('http://', 'https://', '/', 'data:')

# https://github.com/django-compressor/django-compressor/pull/337
class CustomCssAbsoluteFilter(CssAbsoluteFilter):

    def input(self, filename=None, basename=None, **kwargs):
        if self.url.startswith(('http://', 'https://', '//')):
            self.has_scheme = True
        if filename is None:  # like inline css
            return self.content
        filename = os.path.normcase(os.path.abspath(filename))
        if (not self.has_scheme and not (filename and filename.startswith(self.root)) and
            not self.find(basename)):
            return self.content
        self.path = basename.replace(os.sep, '/')
        self.path = self.path.lstrip('/')
        if self.has_scheme:
            parts = self.url.split('/')
            self.url = '/'.join(parts[2:])
            self.url_path = '/%s' % '/'.join(parts[3:])
            self.protocol = '%s/' % '/'.join(parts[:2])
            self.host = parts[2]
        self.directory_name = '/'.join((self.url, os.path.dirname(self.path)))
        return SRC_PATTERN.sub(self.src_converter,
            URL_PATTERN.sub(self.url_converter, self.content))
