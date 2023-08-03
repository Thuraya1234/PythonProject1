# Input & Output File .........

"""
# to read first row in a list of numbers ......
InputFile = open("key3.txt", "r")

for line in InputFile:
    data = line.rsplit()
    print(data[0])
""" 
""" OR
#for line in InputFile:
    #print(line[0])
"""

#....................................................
"""
#to calculate the average of sum of numbers ....

InputFile = open("key2.txt", "r")

total_sum = 0
average = 0
count = 0
for line in InputFile:
    total_sum += float(line)
    count+=1

average = (total_sum/count)  
print(average)

"""