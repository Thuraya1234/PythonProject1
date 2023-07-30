#Random Numbers with check prediction.........
#.....................................
import random

random_no = random.randint(1,10)
user = 0

while (random_no != user):
    user = int(input("Enter predict number: "))
    if random_no > user:
        print("Go Up")
        continue
    elif random_no < user:
        print("Go down")
        continue
    else:  
        print("Correct")
        
   

