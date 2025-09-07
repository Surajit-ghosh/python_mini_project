def fact(n):
    if(n==0 or n==1):
        return 1
    else:
      c=n*fact(n-1)
      return c  
print(fact(5))   
 