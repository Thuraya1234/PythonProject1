#Code to insert values to lists, using append() function ..with quite...
values = []
print("please enter values, Q to quite : ")
user = input("")

while user.upper()!= "Q":
    values.append(float(user))
    user = input("")