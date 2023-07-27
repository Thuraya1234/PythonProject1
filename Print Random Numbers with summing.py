# Generate random numbers, input sum of them, print correct, done ...
import random

n = 1  
while(n == 1):
    randomlist = []
    for i in range(0,2):
       r = (random.randint(1,100))
       randomlist.append(r)
    res = randomlist 
    print ("Random numbers : ",res)
    s = input("what is the sum of two numbers? ")
    t = (sum(res))
    
    if not(s =="done"):
        
       if(s == str(t)):     
          print("Correct Answer")
       else:
          print("Rong Answer")
          
    else:
        break




