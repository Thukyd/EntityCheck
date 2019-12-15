##########
# check for duplicates and empty elements

import os,glob
import csv
folder_path = "csv_entities/"
found_values = set()

class ReadInAllFiles():
    def __init__(self, folder):
        for filepath in glob.glob(os.path.join(folder_path, "*.csv")):
            # set filename
            filpathSplit = filepath.split("\\")
            filename = filpathSplit[1]
            newFileName = "output_files/new_" + filename

            with open(filepath) as fin, open(folder_path + newFileName, "w",newline="") as fout:
                reader = csv.reader(fin, delimiter=";")
                writer = csv.writer(fout, delimiter=";")


                ############TODO
                # 1. check for double
                # 2. save doubles in a list
                # 3. write a new function 
                    # for doubles the user has to be asked
                    # for empty elements and rows it should be deleted immediately

                for row in reader:
                    # delete empty list elements & filter out already seen elements
                    # new_row = [x for x in row if x and x not in found_values]
                    allData = []
                    for x in row:
                        if not x: # empty element
                            # do not add to list!!!
                            print("empyt element")
                           
                        elif x not in found_values: # unique element
                            print("new " + x)
                            allData.append(x)
                        else: # found element again
                            print("shit, I found " + str(x) + " again")
                            
                    if not row:
                        print("empty row")

                    print(allData)
                    writer.writerow(allData)
                    

            


ReadInAllFiles(folder_path)
