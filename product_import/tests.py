from django.test import TestCase

import dropbox, csv
from django.conf import settings
from .dropbox_interface import DropboxInterface
from .models import DropboxFileMetadata

# Dropbox tests
class TestDropbox(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.dropbox_interface = DropboxInterface()
        cls.dbx = dropbox.Dropbox(settings.DROPBOX_TOKEN)

    def setUp(self):
        pass

    def test_list_folder(self):
        files = self.dropbox_interface.list_folder()
        self.assertIsInstance(files[0] if files else None, dropbox.files.FileMetadata)

    def test_sync_metadata_to_db(self):
        files = self.dropbox_interface.list_folder()
        self.dropbox_interface.save_metadata(files)
        # test to make sure we got back the data we need
        self.assertIsInstance(DropboxFileMetadata.objects.first(), DropboxFileMetadata)
        # make sure duplicates are not created
        self.dropbox_interface.save_metadata(files)
        self.assertEqual(len(files), DropboxFileMetadata.objects.count())

        # did the export_type and company get saved to the db?
        file_to_test = files[0]
        filemeta = DropboxFileMetadata.objects.get(name=file_to_test.name)
        self.assertEqual(
            (filemeta.export_type, filemeta.company),
            DropboxFileMetadata._get_type_company_from_filename(files[0].name))

    def test_get_type_company_from_filename(self):
        filenames_type_company = [
            ('20161012070014.SHPFY_ProductExtract_Theia.CSV', 'Product', 'Theia'),
            ('20161012070015.SHPFY_InventoryExtract_Theia.CSV', 'Inventory', 'Theia'),
            ('20161012070015.SHPFY_ProductExtract_DavidMeister.CSV', 'Product', 'DavidMeister'),
            ('20161012070015.SHPFY_ProductExtract_KayUnger.CSV', 'Product', 'KayUnger'),
            ('20161012070020.SHPFY_InventoryExtract_DavidMeister.CSV', 'Inventory', 'DavidMeister'),
            ('20161012070021.SHPFY_InventoryExtract_KayUnger.CSV', 'Inventory', 'KayUnger')]
        for filename, export_type, company in filenames_type_company:
            self.assertEqual(DropboxFileMetadata._get_type_company_from_filename(filename), (export_type, company))

    def test_get_latest_inventory_filemetadata(self):
        files = self.dropbox_interface.list_folder()
        self.dropbox_interface.save_metadata(files)
        # now sort and filter the files array to get the latest file metadata
        files.sort(key=lambda x: x.server_modified, reverse=True)
        expected_file_metadata = filter(lambda x: 'Theia' in x.name and 'Inventory' in x.name, files)[0]
        # get the latest from the db interface
        filemeta = DropboxFileMetadata.objects.export_type('Inventory').company('Theia').latest()
        self.assertEqual(expected_file_metadata.name, filemeta.name)

    def test_get_latest_inventory_csv_file(self):
        files = self.dropbox_interface.list_folder()
        self.dropbox_interface.save_metadata(files)
        filemeta = DropboxFileMetadata.objects.export_type('Inventory').company('Theia').latest()
        text = self.dbx.files_download(filemeta.dropbox_id)[1].text
        print(text)
        pass

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        pass


class TestInventory(TestCase):
    pass
