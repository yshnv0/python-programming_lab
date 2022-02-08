l1=[1,2,3,4,5]
l2=[11,12,13,14,15,5]

print(l1)
print(l2)


if len(l1)==len(l2):
    print("list are of same length")
else:
    print("List are not of same length")



if sum(l1)==sum(l2):
    print("List are of same sum")
else:
    print("List are not of same sum")


l3=[x for x in l1 if x in l2]
if len(l3)<1:
    print("No value occure in both")
else:
    print("common values:",l3)