from django.core.files.storage import get_storage_class
from storages.backends.s3boto import S3BotoStorage
import urllib
import urlparse

class CachedS3BotoStorage(S3BotoStorage):
    """
    S3 storage backend that saves the files locally, too.
    """

    querystring_auth=False

    def __init__(self, *args, **kwargs):

        # merge in any arguments that were passed
        kwargs.update(dict(location='public', querystring_auth=False))

        super(CachedS3BotoStorage, self).__init__(*args, **kwargs)
        self.local_storage = get_storage_class(
            "compressor.storage.CompressorFileStorage")()

    def save(self, name, content):
        name = super(CachedS3BotoStorage, self).save(name, content)
        self.local_storage._save(name, content)
        return name

    def url(self, name):
        orig = super(CachedS3BotoStorage, self).url(name)
        scheme, netloc, path, params, query, fragment = urlparse.urlparse(orig)
        params = urlparse.parse_qs(query)
        if 'x-amz-security-token' in params:
            del params['x-amz-security-token']
        query = urllib.urlencode(params)
        return urlparse.urlunparse((scheme, netloc, path, params, query, fragment))
