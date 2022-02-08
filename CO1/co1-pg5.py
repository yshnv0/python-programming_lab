l = []
l = [int(item) for item in input("Enter the list items : ").split()]
print("INPUT IS", l)
x = ["over" if x > 100 else x for x in l]
l = list(x)
print(l)