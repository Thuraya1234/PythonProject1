#Calculate the sum of unknown numbers in function ..........
 
def fun(*numbers):
    total = 0
    for i in numbers:
        total += i
    return total
print(fun(1,2,3))