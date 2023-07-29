# Program to Check Leap Year ...

year = int (input ("Enter year to be checked for leap year: "))

if (year % 4) == 0:

    if (year % 100) == 0:

        if (year % 400) == 0:
            print("It is a leap year")
        else:
            print("It is not a leap year")
    else:
         print("It is not a leap year")
else:     
    print("It is not a leap year")
