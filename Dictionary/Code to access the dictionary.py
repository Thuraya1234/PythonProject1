# Code to access the dictionary and determine the age which greatest than 22 ...... 
dec = {1: {"name": "John", "age": 27, "sex": "Male"},
       2: {"name": "Marie", "age": 22, "sex": "Female"},
       3: {"name": "Sali", "age": 23, "sex": "Female"},
       }

for key, item in dec.items():
    if item["age"]>22:
       print(item["name"])
     
     
     
     