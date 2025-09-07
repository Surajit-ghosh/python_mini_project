class Student:
    college_name="BBIT"
    def __init__(self,fullname,marks,number):
        self.name=fullname
        self.mark=marks
        self.number=number
        print("Added database")
    def welcome(self):
        print("Welcome\t",s1.name)    
s1=Student("Surajit Ghosh",88,8918636831)
s1.welcome()
print(s1.name,s1.mark,"College name =",s1.college_name,s1.number)  



s2=Student("Mantu",99,76)     
print(s2.name,s2.mark,s2.college_name)