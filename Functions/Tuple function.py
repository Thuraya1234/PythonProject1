# Use Tuple function ...

def readDate():
    print("ENTER :")
    month = input(" month ")
    day = input(" day")
    year = input(" year ")
    return (month, day, year) #Tuple function..

#OR...
#(month, day, year) = readDate()
#print(readDate())

date = readDate()
print(date)
