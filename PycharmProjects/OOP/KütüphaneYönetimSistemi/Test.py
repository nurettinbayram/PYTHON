from OOP.KütüphaneYönetimSistemi.Book import Book
from OOP.KütüphaneYönetimSistemi.Librarian import Librarian
from OOP.KütüphaneYönetimSistemi.Student import Student
from OOP.KütüphaneYönetimSistemi.Teacher import Teacher

library = []
print("\n---------------Kütüphaneci kitap ekliyor-----------")

librarian = Librarian("Büşra")
book1 = Book("Python 101", "Ahmet Yılmaz", 2)
book2 = Book("OOP in Depth", "Zeynep Arslan", 1)
librarian.add_book(library, book1)
librarian.add_book(library, book2)

print("\n---------------Öğrenci kitap alıyor-----------")

student = Student("Nurettin")
student.borrow_book(book1)
student.borrow_book(book2)
student.borrow_book(book2)  # stok biter
student.show_debt()
student.pay_fee(15)

print("\n---------------Öğretmen kitap alıyor-----------")

teacher = Teacher("Bülent")
teacher.borrow_book(book1)

print("\n---------------Kütüphaneci kitap çıkarıyor-----------")

librarian.remove_book(library, book2)

print("\n---------------Kitapları göster-----------")

print("\n--- Library Books ---")
for book in library:
    print(book)