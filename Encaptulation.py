class student:
    def __init__(self):
        self.__name=""
    def gate(self):
        return self.__name
    def set(self,name):
        self.__name=name    
obj=student()
obj.set("Surajit")
name=obj.gate()
print(name)    
    