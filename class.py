class Student:
    id
    name=" "
    def __init__(self,id,name):
        self.id=id
        self.name=name
    def display(self):
        print(self.id,self.name)
s=Student(509,"Satwika")
s.display()

