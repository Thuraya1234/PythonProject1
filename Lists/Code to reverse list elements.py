# Code to reverse list elements...
values = [6, 3, 8, 1, 7]

reversedList = []

for i in range(len(values)):
        r= values[len(values) - i - 1]
        reversedList.append(r)
print(reversedList)

