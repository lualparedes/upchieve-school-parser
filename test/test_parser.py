import unittest

from config import FILE_PATH, SCHOOLS_TABLE
from parser.__main__ import (
    import_data_from, 
    export_data_to, 
    determine_if_is_highschool,
    get_highschools_from
)



class TestParser(unittest.TestCase):
    """Test suite for parser"""

    def test_import_data_from(self):
        self.assertEqual(import_data_from(FILE_PATH), SCHOOLS_TABLE)


    def test_export_data_to(self):
        pass


    def test_determine_if_is_highschool(self):
        pass


    def test_get_highschools_from(self):
        pass



if __name__ == '__main__':
    unittest.main()
