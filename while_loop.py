n=int(input("enter the input"))
i=1
while i<=n+1:
    if i!=n:
        print(i, end=",")
    else:
        print(i,end="")
    i=i+2