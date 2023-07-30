# Python program for checking of Narcissistic number ...

# Function for checking ........................
def getResult(user_input):
    sum = 0
    length = len(user_input)
 
    # Traversing through the string
    for i in user_input:
 
        # Converting character to int
        sum = sum + int(i) ** length
 
    # Converting string to integer
    number = int(user_input)
 
    # Comparing number and sum
    if (number == sum):
        return "true"
    else:
        return "false"
 
# taking input as string......................
user_input = input("Enter a number to check if a Narcissistic number or not : ")
print(getResult(user_input))