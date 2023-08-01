#Python code that go throw all numbers from 1 to 30 and print True if the number is prime and False if not.....
lower = 1
upper = 30

print("Number", "  |  ", "Prime Status:")
print("-------------------------")

for num in range(lower, upper +1):
   # all prime numbers are greater than 1
    if num > 1 :
       for i in range(2, num):
           if (num % i) == 0:
               print(num, "       |      ", False)
               break
       else:
           print(num, "       |      ", True)           
           
    else:
        print(num, "       |      ", False)
       
