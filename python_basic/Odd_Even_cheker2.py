def checker(n):
    if (n%2==0):
        print(n," is Even number")
    else:
        print(n," is Odd number")          
while True:
    p=int(input("press 1 for continue and 0 for stop : "))
    if (p==1):
      x=int(input("Enter a number to check odd or even : "))
      checker(x) 
    elif(p==0):
        print("Thank you for your responce")
        break
    elif(p!=0 or p!=1):
        print("Maderchod chose 1 or 0")      

         
