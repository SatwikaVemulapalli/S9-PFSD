class Sample:
    def __init__(self,id,name,cgpa):
        self.id=id
        self.name=name
        self.cgpa=cgpa
s=Sample(509,"Satwika",9.8)
print(getattr(s,"name"))
setattr(s,"cgpa",10)
print(getattr(s,"cgpa"))
delattr(s,"id")
print(hasattr(s,"id"))