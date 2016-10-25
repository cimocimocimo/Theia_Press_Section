from __future__ import unicode_literals

from django.db import models
import re

class DropboxFileMetadataQueryset(models.query.QuerySet):
    # We may add more
    # get product export files

    # get inventory export files
    pass

class DropboxFileMetadataManager(models.Manager):
    # def get_queryset(self):
    #     return DropboxFileMetadataQueryset(self.model, using=self._db)

    # def product_extract(self):
    #     return self.get_queryset().product_extract
    pass

class DropboxFileMetadata(models.Model):

    objects = DropboxFileMetadataManager()
    _type_company_pattern = re.compile(r'^\d{14}\.SHPFY_([A-Za-z]+)Extract_([A-Za-z]+)\.CSV$')

    # 20161022190044.SHPFY_InventoryExtract_KayUnger.CSV
    name = models.CharField(max_length=255, unique=True)
    # id:7W97kciKqBAAAAAAAAAEpQ
    # these are unique, MySQL only handles case INsensitive strings in unique
    # varchar fields. All the values are unique but they differ only by case
    # sensitivity. That's why we are using the name as the unique field in this
    # case. Case sensitivity shouldn't matter there since the filenames are
    # different enough (e.g.: Theia and theia won't be different brands).
    dropbox_id = models.CharField(max_length=255)
    client_modified = models.DateTimeField()
    server_modified = models.DateTimeField()
    # e68486c9027
    rev = models.CharField(max_length=256)
    size = models.PositiveIntegerField()
    # =u'/e-commerce/20161022190044.shpfy_inventoryextract_kayunger.csv'
    path_lower = models.CharField(max_length=2048)
    # =u'/E-Commerce/20161022190044.SHPFY_InventoryExtract_KayUnger.CSV'
    path_display = models.CharField(max_length=2048)
    # =u'1215074343'
    parent_shared_folder_id = models.CharField(max_length=256)

    export_type = models.CharField(max_length=64)
    company = models.CharField(max_length=128)

    def __str__(self):
        return 'name: {}, dropbox_id: {}, client_modified: {}, server_modified: {}, rev: {}, size: {}, path_display: {}'.format(
            self.name,
            self.dropbox_id,
            self.client_modified,
            self.server_modified,
            self.rev,
            self.size,
            self.path_display,
        )

    @classmethod
    def _get_type_company_from_filename(cls, filename):
        match = cls._type_company_pattern.match(filename)
        if match:
            return match.group(1,2)
        else:
            return None
