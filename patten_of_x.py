for i in range(0,7):
    for j in range(0,7):
        if(i+j==6) or (i-j==0):
            print('*', end=" ")
        else:
            print(" ",end=" ")
    print(" ")