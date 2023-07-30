# Program for Electricity Bill ...

elec = float(input("Enter Electricity Bill: "))

if (elec <= 100):
    print("No Charge")
elif (100<elec<=200):
    print(elec*0.024," RO")
elif (elec>200):
    print(elec*0.047," RO")

