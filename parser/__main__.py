import sys

from config import FIELDS_OF_INTEREST



def import_data_from(filename): 
    """Imports a file and converts it into a "list table"

    Args:
        filename: string
    Returns:
        a "DB table" as a list
    """
    csv = open(filename)
    imported_csv = csv.read()
    csv.close()

    return imported_csv



def export_data_to(filename, data):
    """Exports a "list table" to a file

    Args:
        filename: string
        data: list (a "DB table")
    Returns:
        void
    """
    exported_csv = open(filename, 'w')
    exported_csv.write('\n'.join(data))
    exported_csv.close()



def determine_if_is_highschool(record):
    """Determine if a given school is a highschool
    
    Args:
        record: list that corresponds to a school "DB record"
    Retruns:
        boolean
    """
    for i in FIELDS_OF_INTEREST:
        if record[i] == 'Yes':
            return True
    return False



def get_highschools_from(table_list):
    """Goes through each of the "school records" in a list and returns another 
    list that contains only highschools

    Args:
        table_list: list (a "DB table")
    Returns:
        another "DB table" that contains only highschools
    """
    pass



def main(filename):
    schools = import_data_from(filename)
    highschools = get_highschools_from(schools)
    export_data_to(filename[:-4] + '_out.csv', highschools)



if __name__ == '__main__':
    try:
        assert sys.argv[1] != ''
    except Exception as e:
        raise
    else:
        main(sys.argv[1])