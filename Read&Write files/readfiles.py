
""" # to read file ...
input_file = open("key.txt", "r")
#line = input_file.read() ....to read each line..
#line = input_file.readline() .... to read all data of..

#to print the even numbes from file ....
for line in input_file :
    if int(line) % 2 == 0:       
        print(line)  """
        
        

""" # to rewrite the file to new data .. will replace all data by new data ..
input_file = open("key.txt", "w")
input_file.write("8")"""

input_file = open("key.txt", "a")
input_file.write("8")
input_file.close() # close file