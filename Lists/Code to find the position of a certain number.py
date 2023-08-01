# Code to find the position of a certain number ... 
limit = [10, 20, 30, 90]
found = False
pos = 0

while pos < len(limit) and not found:
    if limit[pos] == 90:
        found = True
    else:
        pos+=1

if found :
    print("Found at position : ", pos)
else:
    print("Position Not found")