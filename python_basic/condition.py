age=int(input("Enter your age: "))
if(age>18):
    if(age>80):
     print("You can give vote but not drive")
    else:
        print("You can give vote") 
elif(age==18):
    print(" From this year you can give vote") 
else:
    print("Wait you can't give vote before ", 18,"Year")       
# age=int(input("Enter your age: "))
# vote=("yes","no")[age<=18]
# print(vote)
#2
color=input("Enter the color: ")
if(color=="red"):
    print("Stop")
elif(color=="green"):
    print("Go")
elif(color=="yellow"):
    print("Look")
else:
    print("Light is not ok")   
#3
food=input("Food name: ")
mood="Yes" if food=="cake" else "no"
print(mood)   
print("bhalo") if food=="cake" or food =="mithai" else print("khabo na")
#
sal=int(input("Enter your salarry : "))
tax=sal*(0.1,0.2)[sal>=50000]
print(tax)