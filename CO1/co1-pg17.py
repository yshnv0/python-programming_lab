d={"a":1,"c":5,"b":2,"e":8,"f":4}

print("Sorting by key")
print("Ascending order : ",sorted(d.items()))
print("Descending order : ", sorted(d.items(),reverse=True))


print("Sorting by value")
import operator
dict1=sorted(d.items(),key=operator.itemgetter(1),reverse=True)
print("Descending order:",dict1)
dict1=sorted(d.items(),key=operator.itemgetter(1),reverse=False)
print("Ascending order:",dict1)
