# Function to calculate the average of scores ....
lisScore = [10, 20, 30, 40, 50]

def calculateAverage(score):
    total_sum = 0
    average_score = 0
    for i in range (len(score)):       
          total_sum += score[i]
    average_score = (total_sum/len(score))
    return average_score

print(calculateAverage(lisScore))




    


    