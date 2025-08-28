# Python setattr() function is used to set an attribute dynamically


class Cloth:
    pass


# Add class method
@classmethod
def brandName(cls):
    print("The name of the brand is Raymond")

# Adding dynamically

setattr(Cloth,"brand_name",brandName)
newObj = Cloth()
newObj.brand_name()


