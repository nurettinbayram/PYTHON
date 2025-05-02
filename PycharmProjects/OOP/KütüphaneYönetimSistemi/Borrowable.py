from abc import ABC, abstractmethod

class Borrowable(ABC):
    @abstractmethod
    def borrow_book(self, book):
        pass