from item import Item


class Phone(Item):  # Inheritance
    def __init__(self, name: str, price: float, quantity=0, broken_phones=0):
        super().__init__(name, price, quantity)

        assert (
            broken_phones >= 0
        ), f"Broken Phones {broken_phones} must greater than zero!"

        self.broken_phones = broken_phones
