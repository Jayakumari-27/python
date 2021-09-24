n=int(input("enter the input"))
i=1
mul=1
while n>=i:
    if i!=n:
        print(n, end="x")
    else:
        print(n,end="")
    #print(n,end="x")
    mul=mul*n
    n=n-1

print(f"={mul}")