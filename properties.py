class InvalidPriceError(Exception):
    pass


class Product:
    def __init__(self, price):
        self.price = price

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value < 0:
            raise InvalidPriceError("Price should not be less than 0")
        self.__price = value
    # price = property(get_price, set_price)


product = Product(100)
product.price = -1
print(isinstance(product, Product))
print(issubclass(Product, object))
print(product.price)
