from abc import ABC,abstractmethod

class democlass(ABC):
    @abstractmethod
    def method1(self):
        print("Abstract Class")

    def method2(self):
        print("Concrete Class")


class concreteclass(democlass):
    def method1(self):
        super().method1()
        return
    

obj = concreteclass()
obj.method1()
obj.method2()