option=int(input("1-veg\n2-NV\n enter your option"))
if option==1:
    print("veg")
    dishes=input("enter the dishes type\n1-breakfast\n2-lunch")
    if dishes=="1":
        varities=input("enter the varities type\n1-idaly--RS6\n2-pongal--RS20")
        print(f"{varities} coming soon")
    elif dishes=="2":
        varities=input("enter the varities type\n-1 sambar--RS30\n2 curd--Rs25")
        print(f"{varities}coming soon")
elif option==2:
    if dishes=="1":
        varities=input("enter the\n1-Idaly+chickencurry--60\n2-parota--20")
        print(f"{varities}coming soon")
    elif dishes=="2":
        varities=input("enter the varities\n 1-briyani RS-100\n 2-NV meals Rs-150")
        print(f"{varities}coming soon")
else:
    print("invalid")