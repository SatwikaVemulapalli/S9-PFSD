class Base:
    def fun1(self):
        print("this is fun1")
class Derived1(Base):
    def fun2(self):
        print("this is fun2")
class Sample(Derived1):
    def fun3(self):
        print("this is fun3")
obj=Sample()
obj.fun1()
obj.fun2()
obj.fun3()