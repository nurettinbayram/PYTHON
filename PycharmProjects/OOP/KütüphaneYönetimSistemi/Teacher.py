from OOP.KütüphaneYönetimSistemi.Borrowable import Borrowable
from OOP.KütüphaneYönetimSistemi.Person import Person


class Teacher(Person, Borrowable):
    def borrow_book(self, book):
        if book.decrease_stock():
            print(f"{self.name} borrowed '{book.title}' (no fee)")
        else:
            print(f"No stock left for '{book.title}'")