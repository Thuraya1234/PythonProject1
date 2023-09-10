for num in range(1, 100):
     divisors_sum = 0
     for divisor in range(1, (num//2)+1):
            if num % divisor == 0:
               divisors_sum += divisor
               if num == divisors_sum:
                  print(num)
                        
                   
