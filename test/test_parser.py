import unittest

from config import FILE_PATH
from parser.__main__ import main



class TestParser(unittest.TestCase):
    """Test suite for parser"""

    def test_import_data_from(self):
        
        main(FILE_PATH)


    def test_export_data_to(self):
        pass


    def test_determine_if_is_highschool(self):
        pass


    def test_get_highschools_from(self):
        pass



if __name__ == '__main__':
    unittest.main()
