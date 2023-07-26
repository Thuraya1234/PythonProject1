# program to store files in PC ...

x = int(input("Enter size of storage: "))
n = int(input("Enter number of files: "))
y = int(input("Enter size of files: "))

full_size = n * y

if full_size <= x :
    print("yes, can be stored")
else:
    print("sorry, can not be stored")


