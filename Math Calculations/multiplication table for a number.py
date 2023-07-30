# Print multiplication table for a number ...

n = int(input("Enter a number: "))

count = 1

while(count<=12):
    digit = count *n
    print(n, "*",count, "=",digit)
    count= count +1