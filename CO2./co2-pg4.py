u=int(input("Enter the upper limit="))
l=int(input("Enter the lower limit="))
l1=[]
l2=[]

for x in range(l, u + 1):
    if x % 2 == 0:
        l1.append(x)

for y in l1:
    for z in range(1,y):
          if (z*z) ==y:
             l2.append(y)
print(l2)
