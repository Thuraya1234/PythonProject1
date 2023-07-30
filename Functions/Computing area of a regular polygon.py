# Computing area of a regular polygon ................
#...............................
import math
num_side = int(input("Enter number of sides: "))
l_sides= float(input("Enter sides: "))

def area(n, side):
    a = (n*(side)**2)/(4*(math.tan(math.pi/n)))
    return a

print(area(num_side, l_sides))
