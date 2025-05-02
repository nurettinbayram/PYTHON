from OOP.KütüphaneYönetimSistemi.Person import Person


class Librarian(Person):
    def __init__(self, name):
        super().__init__(name)

    def add_book(self, library, book):
        library.append(book)
        print(f"{self.name} added '{book.title}' to the library.")

    def remove_book(self, library, book):
        if book in library:
            library.remove(book)
            print(f"{self.name} removed '{book.title}' from the library.")