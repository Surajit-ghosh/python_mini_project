def checker(x):
    import random
    computer=random.randrange(1,101)
    
    if (x>computer):
      print("Computer number is ",computer)
      print("Your number is too high")
    elif(x<computer):
      print("Computer number is ",computer)
      print("Your number is too high")
    elif(x==computer):
      print("Computer number is ",computer)
      print("Your enter number is equal to computer number")  

while True:      
  p=int(input("Enter 1 for continue and 0 for stop : "))
  if(p==1):
    x=int(input("Enter a number : "))
    checker(x)
  elif(p==0):
    print("Thanks for your responce")
    break
  else:
    print("Pleace enter a number 0 or 1")   

  

