class Book:
    def __init__(self, title, author, stock):
        self.title=title
        self.author = author
        self.__stock = stock

    def decrease_stock(self):
        if self.__stock > 0:
            self.__stock -= 1
            return True
        return False

    def increase_stock(self):
        self.__stock += 1

    def get_stock(self):
        return self.__stock

    def __str__(self):
        return f"{self.title} by {self.author} - Stock: {self.__stock}"
