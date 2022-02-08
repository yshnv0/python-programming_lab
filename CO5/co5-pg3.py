#read each row from a given csv file and print a list of strings.
import csv
listofcsv = []
with open('file3.csv') as csv_file:
    file_obj = csv.reader(csv_file)

    for rows in file_obj:
       listofcsv.append(rows)

print(listofcsv)
