print("welcome to treasure")
option=input("where do you want to go\n1-left\n2-not")
if option=="1":
    a=input("welcome to island\n1-swim\n2-not")
    if a=="1":
        print("gameover")
    else:
        b=input("choose color\n1-yellow\n2-red")
        if b=="1":
            print("reached")
        else:
            print("gameover")
else:
    print("gameover")
