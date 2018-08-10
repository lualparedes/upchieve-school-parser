import sys
"""
Awesome! So yes 3 ideal changes:
- if they type and there is no result, instead of having no box, have a box 
where they select "My school is not listed" (i.e. so that choice shows up in 
the search if they exhaust all the other options). To clarify, I do NOT want 
them to just be able to type in any thing. I want verification to require them 
to choose something from the list, because it will help us a lot with analytics. 
All students from the same school must have the same entry in their HS field.
- only show schools that offer at least one of grades 9,10,11,12 . 
- first letter of each word capitalized


"""

# Positions of the fields that determine if G9-12 are offered
FIELDS_OF_INTEREST = [53, 54, 55, 56]



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
    print filename
    pass



def determine_if_is_highschool(record):
    """Determine if a given school is a highschool
    
    Args:
        record: list that corresponds to a school "DB record"
    Retruns:
        boolean
    """
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