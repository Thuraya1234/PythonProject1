# Computing sum of all elements using list index .........

myList = [3, 5, 1, 7, 2, 8]
sum = 0
for i in range(len(myList)):
    sum += myList[i]
    
print("The sum of the list = ", sum)