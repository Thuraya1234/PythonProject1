# Dictionary functions ...
contacts = {"Maather": 99657453, "Thuraya": 98115377, "Asma": 97558222}

con = dict(contacts)

if "Thuraya" in contacts:
    print(contacts["Thuraya"])
else:
    print("Not found")
    
#...............................
#contacts["Amna"] = 98443633
if "Amna" in contacts:
    contacts.pop("Amna")
print(contacts)
#..................................

for key in sorted(contacts):
     print(key , contacts[key])

#......................
for item in contacts.items():
    print(item[0], item[1])
     
     
