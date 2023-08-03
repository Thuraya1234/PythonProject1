# Exception Handling..........

inputOk = False

while (inputOk == False):
    try:
        num = input("Enter a number: ")
        num = float(num)
        
        inputOk = True   # All characters are part of number
    except ValueError:   # Can'tconvert to a number
            print("Non-numeric type entered '%s'" %num)
            
num = num*2
print(num)