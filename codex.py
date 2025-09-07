point=float(input("How much you rate the resturant out of 5 : "))
if (4.5<=point<=5):
    print("Extraordinary")
elif(4<=point<4.5):
    print("Excellent")  
elif(3<=point<4):
    print("Good") 
elif(2<=point<3):
    print("Fair")
else:
    print("Poor")               