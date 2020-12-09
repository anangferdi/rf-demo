import csv

class csv_library(object):
    def read_csv_file(self, filename):
        """
        This creates a keyword named "Read csv file".
        This keyword takes one argument, which is a path to a .csv file.
        It returns a list of rows, with each row being a list of the data in each column. 
        """
        data = []
        with open(filename, 'rt') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                #print("row:"+str(row))
                data.append(row)
        return data

csv_library_instance = csv_library()
csv_library_instance.read_csv_file("test.csv")
