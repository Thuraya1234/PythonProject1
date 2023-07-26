# Program to check gender and age ...

gender = (input("Enter your gender F or M: ")).upper()

if(gender == ("F")):
    age = int(input("Enter your age: "))
    if(30>=age>=24):
        print("Accepted")
    else:
        print("Rejected")
else:
    print("Not Accept Male")
