class Student:
    college_name="BBIT"
    def __init__(self,fullname,marks,number):
        self.name=fullname
        self.mark=marks
        self.number=number
        print("Added database")
    def welcome(self):
        print("Welcome\t")  
    
num=int(input("How many student data you want to store : "))
for i in range (num):
    name = input("Enter your name : ")
    marks = []
    subject=["Math","Phy","Chem"]
    for n in range (1,4):
        n=int(input("Enter your marks : "))
        marks.append(n)


    number = int(input("Enter your number : "))
    s=Student(name,marks,number)
    s.welcome()
    print(s.name,s.mark,s.number)
    print("You are now mamber of this college ")



# s1=Student("Surajit Ghosh",88,8918636831)
# s1.welcome()
# print(s1.name,s1.mark,"College name =",s1.college_name,s1.number)  
# s2=Student("Mantu",99,76)     
# print(s2.name,s2.mark,s2.college_name)