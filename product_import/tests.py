from django.test import TestCase

from .dropbox_interface import DropboxInterface
import dropbox
from .models import DropboxFileMetadata

# Dropbox tests
class TestDropbox(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.interface = DropboxInterface()

    def setUp(self):
        pass

    def test_list_folder(self):
        files = self.interface.list_folder()
        self.assertIsInstance(files[0] if files else None, dropbox.files.FileMetadata)

    # make sure I'm getting unique names and ids back from the list_folder method
    def test_unique_names_ids(self):
        files = self.interface.list_folder()
        ids = [file.id for file in files]
        names = [file.name for file in files]
        self.assertEqual(len(ids), len(set(ids)))
        self.assertEqual(len(names), len(set(names)))

    def test_sync_metadata_to_db(self):
        files = self.interface.list_folder()
        self.interface.save_metadata(files)
        # test to make sure we got back the data we need
        self.assertIsInstance(DropboxFileMetadata.objects.first(), DropboxFileMetadata)
        # did the extract_type and company get saved?

        # make sure duplicates are not created
        self.interface.save_metadata(files)
        self.assertEqual(len(files), DropboxFileMetadata.objects.count())


    def test_get_type_company_from_filename(self):
        filenames_type_company = [
            ('20161012070014.SHPFY_ProductExtract_Theia.CSV', 'Product', 'Theia'),
            ('20161012070015.SHPFY_InventoryExtract_Theia.CSV', 'Inventory', 'Theia'),
            ('20161012070015.SHPFY_ProductExtract_DavidMeister.CSV', 'Product', 'DavidMeister'),
            ('20161012070015.SHPFY_ProductExtract_KayUnger.CSV', 'Product', 'KayUnger'),
            ('20161012070020.SHPFY_InventoryExtract_DavidMeister.CSV', 'Inventory', 'DavidMeister'),
            ('20161012070021.SHPFY_InventoryExtract_KayUnger.CSV', 'Inventory', 'KayUnger'),
        ]
        for filename, extract_type, company in filenames_type_company:
            self.assertEqual(DropboxFileMetadata._get_type_company_from_filename(filename), (extract_type, company))

    def test_get_latest_inventory_file_id(self):
        # create a test file

        # update the file list with the database

        #
        # file_id = self.interface.get_latest_inventory_file_id()

        pass

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

