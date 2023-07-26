# Print all numbers which repetition 3 times in ACS...

num = input("Number of items: ")
# use sort method to sort input numbes in Ascending 
arr = sorted(input("Enter Items: ")) 

# Loop for check the repetition 3 times
for i in range(0, len(arr)):    
    for j in range(i+1, len(arr)):
        for x in range(j+1, len(arr)):
         if(arr[i] == arr[j] == arr[x]):    
            print(arr[x]);
            
       