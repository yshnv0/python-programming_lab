#read specific columns of a given CSV file and print the content of the columns
import csv
with open('file3.csv', newline='') as csvfile:
 data = csv.DictReader(csvfile)
 for row in data:
   print(row['age'])
