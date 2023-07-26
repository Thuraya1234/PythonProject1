# Program for calculate which time come first ...

hour1 = int(input("Enter First Time with Hours:"))
minute1 = int(input("Enter First Time with Minutes:"))
hour2 = int(input("Enter Second Time with Hours:"))
minute2 = int(input("Enter Second Time with Minutes:"))

#Check and comparison between two hourse ..
if(hour1 < hour2):
    print(" hour1 comes first")
    
elif(hour1 == hour2):
    
    if(minute1 <= minute2):
        print("hour1 comes first")
    else:
        print("hour2 comes first")    
else:
    print("hour2 comes first")
    
 
