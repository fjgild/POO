class Book:
    def __init__(self, title, quantity, author, price):
        self.title = title
        self.quantity = quantity
        self.author = author
        self.__price = price
        self.__discount = None

    def set_discount(self, discount):
        if 0 <= discount <= 1:
            self.__discount = discount
        else:
            raise ValueError("Discount must be between 0 and 1.")

    def get_price(self):
        if self.__discount is not None:
            return self.__price * (1 - self.__discount)
        return self.__price

    def __repr__(self):
        return f"Titulo: '{self.title}', Cantidad: {self.quantity}, Autor: {self.author}, Precio: {round(self.get_price(), 3)} €"


book = Book("1984", 5, "George Orwell", 15.99)
book.set_discount(0.2)
print(book)