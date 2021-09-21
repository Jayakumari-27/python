name=input("enter the name")
s1=int(input("enter the s1"))
s2=int(input("enter the s2"))
s3=int(input("enter the s3"))
s4=int(input("enter the s4"))
s5=int(input("enter the s5"))
total=s1+s2+s3+s4+s5
avg=total/5
if s1>=35 and s2>=35 and s3>=35 and s4>=35 and s5>=35:
    if avg>=91 and avg>=100:
        print("student is pass grade is A")
    elif avg >= 81 and avg >= 90:
        print("student is pass grade is B")
    elif avg>=61 and avg>=80:
        print("student is pass grade is C")
    elif avg>=41 and avg>=60:
        print("student is pass grade is D")
    else:
        print("student is pass grade is E need th improve try to get the more marks")

else:
    print("student is fail; and try get the pass marks")
print(f"total={total}")
print(f"avg={avg}")

