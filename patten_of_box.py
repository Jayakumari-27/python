for i in range(1,6+1,1):
    for j in range(0,6,1):
        if i==6 or j==0:
            print('*', end=" ")
        elif i==1 or j==5:
            print('*', end=" ")
        else:
            print(" ",end=" ")
    print(" ")