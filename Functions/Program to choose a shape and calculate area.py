#Program to choose a shape and calculate area .........
import math
print("1.sequare , 2.circle , 3.rectangular , 4.cylinder , 5.triangle, or quite")
#.................................................

def sequare_area(length):
    sq_area = length**2
    return sq_area
def circle_area(radius):
    cir_area = (math.pi *((radius)**2))
    return cir_area
def rectangular_area(length2, width2):
    rec_area = (length2*width2)
    return rec_area
def cylinder_area(radius_cy, hight_cy):
    cy_area = ((2*(math.pi)*radius_cy)*(radius_cy+hight_cy))
    return cy_area
def triangle_area(highet_Tr, length_Tr ):
    tri_area = (highet_Tr*length_Tr)/2
    return tri_area
#..................................................
n = 1
while (n == 1):
    user = input("Choose a number : ")
    if not(user == "quite"):
      user = int(user)
      if (user == 1):        
          user1 = float(input("Enter the length of square: "))
          print(sequare_area(user1))
      elif user == 2:
          user2 = float(input("Enter the radius of circle: "))
          print(circle_area(user2))
      elif user == 3:
          user3 = float(input("Enter the length2 of rectangular: "))
          user33 = float(input("Enter the width2 of rectangular: "))
          print(rectangular_area(user3, user33))
      elif user == 4:
          user4 = float(input("Enter the radius_cy of cylinder: "))
          user44 = float(input("Enter the hight_cy of cylinder: "))
          print(cylinder_area(user4, user44))    
      else:
          user5 = float(input("Enter the highet_Tr of triangle: "))
          user55 = float(input("Enter the length_Tr of triangle: "))
          print(triangle_area(user5, user55))
    else:
      break
        

    

    
