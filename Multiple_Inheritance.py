class Base1:
    def fun1(self):
        print("fun1")
class Base2:
    def fun2(self):
        print("fun2")
class Derived(Base1,Base2):
    def fun3(self):
        print("Derived class")
ob=Derived()
ob.fun1()
ob.fun2()
ob.fun3()