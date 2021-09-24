#display the prime number in 1 to 100
n=int(input("enter the number"))
i=2

while(i<=n//2):
 if (n%i==0):
     print(i)
     n = n + 1

