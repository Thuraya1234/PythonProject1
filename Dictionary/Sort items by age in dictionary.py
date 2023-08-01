# Sort items by age in dictionary using sorted()............

dec = {1: {"name": "John", "age": 27, "sex": "Male"},
       2: {"name": "Marie", "age": 22, "sex": "Female"},
       3: {"name": "Sali", "age": 23, "sex": "Female"},
       }

# using sorted()
# Sort nested dictionary by key
res = sorted(dec.items(), key = lambda dec: dec[1]["age"])

print("The sorted dictionary by marks is : " + str(res))
