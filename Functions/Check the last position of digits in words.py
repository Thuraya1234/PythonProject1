# Check the last position of digits in words .........

string = input("Enter sentences with digits: ")

found = False
position = len(string) - 1
while not found and position<=0:
    if string[position].isdigit():
        found = True
    position = position -1
print(position)