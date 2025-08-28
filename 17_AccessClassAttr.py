# Accessing class attribute using a classmethod


class Cloth:

    price=4000


    @classmethod
    def showPrice(cls):
        return cls.price
    

print(Cloth.showPrice())