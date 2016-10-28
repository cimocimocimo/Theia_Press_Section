import dropbox
from django.conf import settings
from .models import DropboxFileMetadata
import pytz, csv

class DropboxInterface():
    path = '/e-commerce'

    def __init__(self, path=None):
        self.dbx = dropbox.Dropbox(settings.DROPBOX_TOKEN)
        if path:
            self.path = path

    # list all the files in the e-commerce dropbox folder
    def list_folder(self):
        files = []
        list_more = True
        # loop through all pages of results
        while list_more:
            results = self.dbx.files_list_folder(self.path)
            files = files + results.entries
            list_more = results.has_more
        return files

    # save file metadata to db or update if dropbox_id matches
    def save_metadata(self, metadata_list):
        for metadata in metadata_list:
            DropboxFileMetadata.objects.update_or_create(
                # this comparison is case INsensitive. See the comments in the
                # model definition for more info.
                name=metadata.name,
                defaults={
                    'name': metadata.name,
                    'dropbox_id': metadata.id,
                    'client_modified': pytz.utc.localize(metadata.client_modified),
                    'server_modified': pytz.utc.localize(metadata.server_modified),
                    'rev': metadata.rev,
                    'size': metadata.size,
                    'path_lower': metadata.path_lower,
                    'path_display': metadata.path_display})

    def get_latest(self, export_type, company):
        files = self.list_folder()
        files.sort(key=lambda x: x.server_modified, reverse=True)
        return filter(lambda x: export_type in x.name and company in x.name, files)[0]

    def get_csv_by_id(self, dropbox_id):
        filemeta, response = self.dbx.files_download(dropbox_id)
        lines = response.text.splitlines()
        # trim the trailing comma
        lines = [l.rstrip(',') for l in lines]
        return csv.DictReader(lines)

    # populate product database from csv product export
    def populate_db_from_csv(self, prod_csv):
        sku_upcs = []
        for row in latest_csv:
            style = row['STYLE NUMBER']
            # TODO: correct the color names
            color = row['COLOR']
            for x in xrange(1,16):
                size_key = 'SIZE {}'.format(x)
                upc_key = 'UPC {}'.format(x)
                size = row[size_key]
                upc = row[upc_key]
                sku_upc = ('{}-{}-{}'.format(style, size, color), upc)
                sku_upcs.append(sku_upc)
