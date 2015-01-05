from django.core.files.storage import get_storage_class
from storages.backends.s3boto import S3BotoStorage
import urllib
import urlparse
from django.conf import settings


class FixedS3BotoStorage(S3BotoStorage):
    def url(self, name):
        """
        Removes security tokens from static file urls.
        """
        orig = super(FixedS3BotoStorage, self).url(name)
        scheme, netloc, path, params, query, fragment = urlparse.urlparse(orig)
        params = urlparse.parse_qs(query)
        if 'x-amz-security-token' in params:
            del params['x-amz-security-token']
        query = urllib.urlencode(params)
        return urlparse.urlunparse((scheme, netloc, path, params, query, fragment))


class DefaultS3BotoStorage(FixedS3BotoStorage):
    def __init__(self, *args, **kwargs):
        kwargs['location'] = settings.DEFAULT_S3_PATH
        super(DefaultS3BotoStorage, self).__init__(*args, **kwargs)


class StaticS3BotoStorage(FixedS3BotoStorage):
    """
    Storage for static files.
    The folder is defined in settings.STATIC_S3_PATH
    Saves the files locally, too.
    """

    def __init__(self, *args, **kwargs):
        kwargs['location'] = settings.STATIC_S3_PATH
        super(StaticS3BotoStorage, self).__init__(*args, **kwargs)

        # define local storage for compressor files
        self.local_storage = get_storage_class(
            "compressor.storage.CompressorFileStorage")()

    def save(self, name, content):
        """
        save locally for compressor to be able to compare files.
        """
        # call super save method
        name = super(StaticS3BotoStorage, self).save(name, content)
        # as well as saving locally. 
        self.local_storage._save(name, content)
        return name

