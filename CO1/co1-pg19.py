a=int(input("enter 1st number"))
b=int(input("enter 2nd number"))
i=1
while i<=min(a,b):
    if(a%i==0 and b%i==0):
        gcd=i
    i+=1
print("GCD=",gcd)
