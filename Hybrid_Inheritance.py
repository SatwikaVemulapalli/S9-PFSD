class Base:
    def fun1(self):
        print("Klu")
class Derived1(Base):
    def fun2(self):
        print("KL University")
class Derived2(Base):
    def fun3(self):
        print("Hello KLUIANS")
class NewDerived(Derived1,Derived2):
    def fun4(self):
        print("This is hybrid inheritance")
ob=NewDerived()
ob.fun1()
ob.fun3()
ob.fun2()
ob.fun4()