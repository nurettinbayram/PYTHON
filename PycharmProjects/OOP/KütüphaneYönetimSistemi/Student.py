from OOP.KütüphaneYönetimSistemi.Borrowable import Borrowable
from OOP.KütüphaneYönetimSistemi.Payable import Payable
from OOP.KütüphaneYönetimSistemi.Person import Person


class Student(Person, Borrowable, Payable):
    def __init__(self, name):
        super().__init__(name)
        self.__debt = 0  # encapsulated

    def borrow_book(self, book):
        if book.decrease_stock():
            print(f"{self.name} borrowed '{book.title}'")
            self.__debt += 10  # each borrow costs 10
        else:
            print(f"No stock left for '{book.title}'")

    def pay_fee(self, amount):
        if amount >= self.__debt:
            print(f"{self.name} paid full debt.")
            self.__debt = 0
        else:
            self.__debt -= amount
            print(f"{self.name} paid {amount}, remaining debt: {self.__debt}")

    def show_debt(self):
        print(f"{self.name} has {self.__debt} TL debt.")