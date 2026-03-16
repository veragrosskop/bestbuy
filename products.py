class Product:

    def __init__(self, name: str, price: float, quantity: int):
        if not name:
            Exception("Product name is empty")
        else:
            self.name = name

        if price < 0:
            Exception("Product price is negative")
        else:
            self.price = price

        if quantity < 0:
            Exception("Product quantity is negative")
        else:
            self.__quantity = quantity

        self.__active = True

    def get_quantity(self) -> int:
        return self.__quantity

    def set_quantity(self, quantity: int):
        self.__quantity = quantity

    def is_active(self) -> bool:
        return self.__active

    def activate(self):
        self.__active = True

    def deactivate(self):
        self.__active = False

    def show(self):
        print(f"{self.name}, Price: {self.price}, Quantity: {self.__quantity}")

    def buy(self, quantity: int) -> float:
        """This function buys a given quantity, returns its price and updates the quantity of the product."""

        if quantity > self.__quantity:
            Exception(
                f"There aren't enough {self.name}'s in storage. /n"
                f"You need: {quantity}, but there's only: {self.__quantity}"
            )
        elif quantity < 0:
            Exception(f"There aren't enough {self.name}'s in storage. /n")
        else:
            self.__quantity -= quantity
            total_price = self.price * quantity

            return total_price
        return None
