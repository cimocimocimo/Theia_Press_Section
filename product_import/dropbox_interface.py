import dropbox
from django.conf import settings
from .models import DropboxFileMetadata
import pytz

class DropboxInterface():
    path = '/e-commerce'

    def __init__(self):
        self.dbx = dropbox.Dropbox(settings.DROPBOX_TOKEN)

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
            obj, created = DropboxFileMetadata.objects.update_or_create(
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
                    'path_display': metadata.path_display,
                    'parent_shared_folder_id': metadata.parent_shared_folder_id
                }
            )


