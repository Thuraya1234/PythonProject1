# Program to create a calculator ...

num1 = float(input("Enter number1: "))
num2 = float(input("Enter number2: "))
opr = input("Enter operator: ")

if (opr == '+'):
    print(num1 + num2)
elif (opr == '-'):
    print(num1 - num2)
elif (opr == '*'):
    print(num1 * num2)
elif (opr == '/'):
    print(num1 / num2)
else:
    print("Invalid Operator")
       
