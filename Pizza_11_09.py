pizza=input("select the type of pza you want\n 1-small pizza\n 2-medium pizza\n 3-large pizza")
bill=0
if pizza=="1":
    bill+=30
elif pizza=="2":
    bill+=40
else:
    bill=50
print(f"you bill {bill}")
pepper_onion=input(f"if you want to pepper onion select\n yes\n no")
if pizza=="1" and pepper_onion=="yes":
    bill+=10
elif pizza=="2" and pepper_onion=="yes":
    bill+=20
elif pizza=="3" and pepper_onion=="yes":
    bill+=30
else:
    bill=bill
print(f"bill amount is {bill}")
