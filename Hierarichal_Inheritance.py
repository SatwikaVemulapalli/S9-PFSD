class Base:
    def fun1(self):
        print("hello")
class Derived1(Base):
    def fun2(self):
        print("world")
class Derived2(Base):
    def fun3(self):
        print("KL University")
ob1=Derived1()
ob1.fun2()
ob1.fun1()
ob2=Derived2()
ob2.fun3()
ob2.fun1()