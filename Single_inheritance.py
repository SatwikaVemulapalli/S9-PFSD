class Base:
    def base1(self):
        print("this is base class")
class Derived(Base):
    def derived1(self):
        print("this is derived class")
obj=Derived()
obj.base1()
obj.derived1()