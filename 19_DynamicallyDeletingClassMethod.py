# Delete class method from class


class Cloth:

    @classmethod
    def brandName(cls):
        print("The brand name is Raymond")

Cloth.brandName()

# deleting dynamically
del Cloth.brandName



print("Method deleted")