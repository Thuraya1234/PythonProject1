# Programe for calculate BMI ... 

weight = float(input("Enter weight in kg: "))
height = float(input("Enter height in cm: "))

hi = height/100
BMI= (weight/(hi**2))

if (BMI<18.5):
    print("Underweight")
elif (25.0>BMI>=18.5):
    print("Normal")
elif (30.0>BMI>=25.0):
    print("Overweight")
elif (BMI>=30.0):
    print("Obese")
    


