# Code for calculate sum of digits of an input number ...

n = int(input("Enter a number: "))
total= 0

while(n>0):
    digit = n % 10
    total += digit
    n = n//10
print(total)