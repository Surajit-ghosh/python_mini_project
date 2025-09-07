# break statment:
for i in range(12):
    if(i==10):
        print("Break the ststement")       
        break
    print("5 x",i,"=",5*(i))
print("I am break") 
# continue statement:   
for i in range(12):
    if((i+1)==10):
        print("Continue the atatement")
        continue
    print("5 x",(i+1),"=",5*(i+1))
print("I am continue")    