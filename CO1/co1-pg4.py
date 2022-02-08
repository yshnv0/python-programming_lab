s=str(input("enter a string"))
l=s.split(" ")
print(l)
d={x:l.count(x) for x in l}
print(d)
