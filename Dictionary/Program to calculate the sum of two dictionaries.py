# Program to calculate the sum of two dictionaries.....

m1 = [[1, 2, 3],
     [4, 5, 6]]

m2 = [[1, 2, 3],
     [4, 5, 6]]

result =[[0, 0, 0], [0, 0, 0]]

if len(m1) == len(m2):
    
    for i in range(len(m1)):
       for j in range(len(m1[0])):       
          result[i][j] = m1[i][j] + m2[i][j]       
        
    print(result)
else:
    print("Invalid ...")