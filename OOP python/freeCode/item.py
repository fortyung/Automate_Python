import csv


class Item:
    # class attribute
    sale = 0.8
    all = []

    def __init__(self, name: str, price: float, quantity=0):
        # Validations
        if not isinstance(name, str):
            raise TypeError("Name is not a string!")

        assert price >= 0, f"Price {price} must greater than zero!"

        # Instance Attribute
        self.__name = name  # Encapsulation: The double underscore makes the variable unaccessable outside the class
        self.__price = price
        self.quantity = quantity

        Item.all.append(self)

    def __connect(self):  # Abstraction: This class is not accessable outside this class
        print("This should be private")

    def __prepare_body(self):
        pass

    def __send(self):
        pass

    def send_mail(self):
        self.__connect
        self.__prepare_body
        self.__send
        return self.__connect

    @property
    # Property Decorator = Read-Only Attribute
    def name(self):
        # Calling this arttibute will basically call the function
        return self.__name

    @name.setter
    def name(self, value):
        # setting this arttibute will basically call the function
        if len(value) >= 10:
            raise Exception("Line is too long!")
        else:
            self.__name = value

    @name.deleter
    def name(self):
        print(f"deleting {self.__name}")
        self.__name = None

    @property
    def price(self):
        return self.__price

    def apply_sale(self):
        self.__price = self.__price * self.sale
        return self.__price

    def apply_increment(self, increment_value):
        self.__price = self.__price + (self.__price * increment_value)
        return self.__price

    @classmethod
    def instantiate_from_csv(cls):
        with open("item.csv", "r") as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            Item(
                name=item["name"],
                price=float(item["price"]),
                quantity=int(item["quantity"]),
            )

    @staticmethod
    def check_integer(num):
        if isinstance(num, float):
            # returns True if the float number represents an integer
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self.name}', '{self.__price}', '{self.quantity}')"
