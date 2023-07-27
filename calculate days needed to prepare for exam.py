n = int(input("Enter number of subjects: "))
x = int(input("Enter number of needed days: "))
y = int(input("Enter number of days left to first exam: "))

if (n * x <= y):
    print("pass")
else:
    print("fail")
