l=[]
a=[]
n=int(input("Enter size of list"))
for x in range(0,n):
    s=input("Enter a word")
    a.append(len(s))
    l.append(s)
print(l)
print("Length of longest word=",max(a))
