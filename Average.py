def average(*numbers):                    #1
  sum=0
  for i in numbers:
    sum = sum +i
    print(sum)
  print("Average is",sum/len(numbers))  
average(5,7,3)  
def average(*numbers):                    #2
  sum=0
  for i in numbers:
    sum = sum +i
  return sum/len(numbers) 
c = average(5,7,3)  
print(c)