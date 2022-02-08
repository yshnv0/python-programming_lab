l1=["red","yellow","blue","green","black"]
l2=["red","black","orange","cyan","white"]


print(l1)
print(l2)
print("all colors from l1 not contained in color-list2")
print("colors in l1,not in l2",[x for x in l1 if x not in l2])

