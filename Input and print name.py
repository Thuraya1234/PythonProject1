#To input and print user name & age with 3 stars* ...

user = input(" enter user name : ")
age = input("enter your age : ")
d = "*"
print("your name %-8s" %(user), "%-3s" %(d*3) ," Age %-3s"%(age))

