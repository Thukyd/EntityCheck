##########
# check for duplicates and empty elements

import os,glob
import csv
folder_path = "csv_entities/"
found_values = set()

for filepath in glob.glob(os.path.join(folder_path, "*.csv")):
    # set filename
    filpathSplit = filepath.split("\\")
    filename = filpathSplit[1]
    newFileName = "output_files/new_" + filename

    with open(filepath) as fin, open(folder_path + newFileName, "w",newline="") as fout:
        reader = csv.reader(fin, delimiter=";")
        writer = csv.writer(fout, delimiter=";")

        for row in reader:
            # delete empty list elements & filter out already seen elements
            new_row = [x for x in row if x and x not in found_values]
            # update marker set with row contents
            found_values.update(row)
            if new_row:
                # new row isn't empty: write it
                writer.writerow(new_row)