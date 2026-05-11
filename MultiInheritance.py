class Class1:
    def m(self):
        print("Method of Class1")

class Class2(Class1):
    def m(self):
        print("Method of Class2")
        super().m() # calling the method of Class1

class Class3(Class1):
    def m(self):
        print("Method of Class3")
        super().m() # calling the method of Class1

class Class4(Class2, Class3):
    def m(self):
        print("Method of Class4")
        super().m() # calling the method of Class2, which will call Class3 and then Class1

def explicit_basecall():
    class Class1:
        def m(self):
            print("Method of Class1")

    class Class2(Class1):
        def m(self):
            print("Method of Class2")
            Class1.m(self) # explicitly calling the method of Class1

    class Class3(Class1):
        def m(self):
            print("Method of Class3")
            Class1.m(self) # explicitly calling the method of Class1

    class Class4(Class2, Class3):
        def m(self):
            print("Method of Class4")
            Class2.m(self) # explicitly calling the method of Class2, which will call Class1
            Class3.m(self) # explicitly calling the method of Class3, which will call Class1

    obj = Class4()
    obj.m()


# print(Class4.mro()) # Method Resolution Order
# print(Class4.__mro__) # Method Resolution Order
# obj = Class4()
# obj.m()

explicit_basecall()