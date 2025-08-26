class Desktop:
    def __init__(self):
        self.__max_price = 25000
    
    def sell(self):
        return f"Selling Price: {self.__max_price}"
    
    def set_max_price(self,price):
        if price > self.__max_price:
            self.__max_price = price


# Object
desktopObj = Desktop() # - Object Created
print(desktopObj.sell())


# modifying the price directly - Data Hiding
desktopObj.__max_price = 35000 # Created a new variable without modifying
print(desktopObj.sell())


# modifying the price using setter function - Controlled Access using Methods
desktopObj.set_max_price(35000)
print(desktopObj.sell()) 