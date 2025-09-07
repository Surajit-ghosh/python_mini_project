def calculate_average():
    n=int(input("How many numbers you want to take"))
    num_list=[]
    sum=0.0
    i=0
    # Take user input as a string of numbers separated by spaces
    #for numbers in range(n):
    while i<n:
     numbers = float(input("Enter numbers separated by spaces: "))
     num_list.append(numbers)
     sum=sum+numbers
     i=i+1
    #calculate the lenth of the number 
    #c=len(num_list)
    # Convert the string of numbers into a list of floats
    # Calculate the average
    #average = sum /c
    print(num_list)
    average=sum/n
    return average
# Call the function and print the result
for i in range(3):
      print("The average is:", calculate_average())
      i+=1

