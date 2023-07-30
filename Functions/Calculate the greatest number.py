# Calculate the greatest number .......
num1 = input("Enter number 1: ")
num2 = input("Enter number 2: ")
num3 = input("Enter number 3: ")

def check_Largest(n1, n2, n3):
        if n1 > n2:
            if n1>n3:
                return n1
            else:
                return n3
        else:
            if n2 > n3:
                return n2
            else:
                return n3

print(check_Largest(num1, num2, num3))