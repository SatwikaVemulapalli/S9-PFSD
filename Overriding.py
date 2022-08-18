class Base:
    def display(self):
        print("KLU")
class Derived(Base):
    def display(self):
        print("KL University")
ob=Derived()
ob.display()