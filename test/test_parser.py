import unittest

from config import (
    FILE_PATH_IN, FILE_PATH_OUT, 
    SCHOOLS_STR, SCHOOLS,
    SAMPLE_RECORDS
)
from parser.__main__ import (
    import_data_from, 
    export_data_to, 
    determine_if_is_highschool,
    get_highschools_from
)



class TestParser(unittest.TestCase):
    """Test suite for parser"""

    def test_import_data_from(self):
        self.assertEqual(import_data_from(FILE_PATH_IN), SCHOOLS_STR)


    def test_export_data_to(self):
        export_data_to(FILE_PATH_IN[:-4] + '_out.csv', SCHOOLS)
        self.assertEqual(
            SCHOOLS_STR,
            import_data_from(FILE_PATH_OUT)
        )


    def test_determine_if_is_highschool(self):
        self.assertEqual(determine_if_is_highschool(SAMPLE_RECORDS[0]), True)
        self.assertEqual(determine_if_is_highschool(SAMPLE_RECORDS[1]), True)
        self.assertEqual(determine_if_is_highschool(SAMPLE_RECORDS[2]), True)
        self.assertEqual(determine_if_is_highschool(SAMPLE_RECORDS[3]), True)
        self.assertEqual(determine_if_is_highschool(SAMPLE_RECORDS[4]), False)


    def test_get_highschools_from(self):
        pass



if __name__ == '__main__':
    unittest.main()
