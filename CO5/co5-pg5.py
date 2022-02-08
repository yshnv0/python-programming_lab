#write a Python dictionary to a csv file. After writing the CSV file 
#-read the CSV file and display the content.
import csv 
dict_value = [
{"name":"vaishnav","age":21,"course":"MCA"},
{"name":"afeef","age":24,"course":"MCA"},
{"name":"sanal","age":21,"course":"MCA"},
{"name":"shibili","age":23,"course":"MCA"},
]

fields = ["name","age","course"]

with open('dict.csv','r+') as csvfile:
    writer = csv.DictWriter(csvfile,fieldnames=fields)
    writer.writeheader()
    writer.writerows(dict_value)
    csvfile.close()

with open('dict.csv','r') as csvfiles:
    readerobj = csv.reader(csvfiles)
    for rows in readerobj:
        print(rows)
