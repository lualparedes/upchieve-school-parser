import sys

from config import FIELDS_OF_INTEREST



def import_data_from(filename): 
    """Imports a file and converts it into a "list table"

    Args:
        filename: string
    Returns:
        a "DB table" as a list
    """
    print 'Importing data from "{0}"...'.format(filename)

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
    print 'Exporting data to "{0}"...'.format(filename)
    exported_csv = open(filename, 'w')
    exported_csv.write('\n'.join(data))
    exported_csv.close()



def is_highschool(record):
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



def get_highschools_from(list_of_schools):
    """Goes through each of the "school records" in a list and returns another 
    list that contains only highschools

    Args:
        list_of_schools: list (a "DB table")
    Returns:
        another "DB table" that contains only highschools
    Notes:
        Range starts in 1 because of the header
    """
    list_of_highschools = [list_of_schools[0]]

    for i in range(1,len(list_of_schools)):
        print 'Processing school {0}...'.format(i)

        if is_highschool(list_of_schools[i].split(',')):
            list_of_highschools.append(list_of_schools[i])
    
    return list_of_highschools



def main(filename):
    schools = import_data_from(filename).split('\n')
    highschools = get_highschools_from(schools)
    export_data_to(filename[:-4] + '_out.csv', highschools)



if __name__ == '__main__':
    try:
        assert sys.argv[1] != ''
    except Exception as e:
        print 'ERROR: a valid filename must be provided as argument'
        raise
    else:
        main(sys.argv[1])