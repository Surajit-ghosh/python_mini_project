class Student:
    college_name = "BBIT"

    def __init__(self, fullname, marks, number):
        self.name = fullname
        self.marks = marks      # dictionary: {subject: mark}
        self.number = number
        print("Added database")

    def welcome(self):
        print(f"Welcome {self.name}, you are now a member of {Student.college_name}!")  

    def show_report(self):
        print("\n--- Report Card ---")
        for subject, mark in self.marks.items():
            print(f"{subject}: {mark}")
        total = sum(self.marks.values())
        avg = total / len(self.marks)
        print(f"Total: {total}, Average: {avg:.2f}")


num = int(input("How many student data you want to store : "))
for i in range(num):
    name = input("\nEnter your name : ")

    marks = {}   # 👈 store subject: mark
    subjects = ["Math", "Physics", "Electronics"]   # 👈 fixed subjects (can be dynamic too)
    for subject in subjects:
        m = int(input(f"Enter marks in {subject}: "))
        marks[subject] = m

    number = int(input("Enter your number : "))

    s = Student(name, marks, number)
    s.welcome()
    print("Name:", s.name)
    print("Number:", s.number)
    s.show_report()
    print("You are now member of this college")
