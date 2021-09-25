for i in range(0,7):
    for j in range(0,7):
        if(j==0) or (j==6) or (j-i==1):
            print('*', end=" ")
        else:
            print(" ",end=" ")
    print(" ")