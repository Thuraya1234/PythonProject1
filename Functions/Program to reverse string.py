# Program to reverse string.........

def revers(s):    
   reversedString = ""
   for char in s:
        reversedString = char + reversedString
   #OR #s = "".join(reversed(s))
   #return s
   return reversedString


s = input("Enter a string : ")

print("The original string :", s)

print("The reversed string : ", revers(s))