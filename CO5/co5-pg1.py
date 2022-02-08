#read_a_file_line_by_line_and_store_it_into_a_list
file_obj = open("file1.txt","r")
file_list = []

condition = True

while condition:
    x = file_obj.readline()
    file_list.append(x)
    if not x:
        condition = False

print("the file converted to list is :")
print(file_list)
