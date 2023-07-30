# Check the validation of Credit Card Number ...............
#...............................................
string = input("Enter Credit Card Number: ")
length = len(string) 

if length == 8 and string[0:4]=="xxxx" and string[4]== " " and string[5:].isdigit():
  print("the string is valid")
else:
 print("the string is not valid")
