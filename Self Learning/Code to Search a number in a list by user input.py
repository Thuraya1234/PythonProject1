# Code to Search a number in a list by user input .........
#..........................................................

list1 = [5, 4, 3, 2, 1]
print(list1)
user = int(input("Input a number for search within above list : "))
pos = 0

if user in list1: 
  while pos < len(list1):
    
    if list1[pos] == user:
        print('Found at Position : ',pos)
        break
    
    else:
        pos+=1
        continue

else :
    print ("not found")
    
print("-------------------------")