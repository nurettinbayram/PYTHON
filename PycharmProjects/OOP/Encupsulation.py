#----------------------OZET-------------------
#   self.name ---------> public
#   self._name --------> protected (onerilmiyor)
#   self.__name -------> private clasin disindan erisilemez


# --------------------Protected Property---------------------
class Person:
    def __init__(self, name):
        self._name = name # burasi protected oldu yani name disaridan erisebilir ama onerilmez

p = Person("nurettin")
print(p._name) # burada intelegens uyari veriyor protected oldugunu
# tek alt cizgi protected yapar


# -------------------Private Property -------------------------

class BankAcount:
    def __init__(self, balance):
        self.__balance = balance  #private
    def getBalance(self):
        return self.__balance
    def setBalance(self, amount):
        if amount >=0:
            self.__balance = amount
    def deposit(self, amount):
        if amount>0:
            self.__balance+=amount

acount = BankAcount(1450)
# print(acount.__balance)  # hata verir veriye ulasamaz

print(acount.getBalance(), "$") ## bu sekilde erisebiliriz
acount.deposit(550)
print(acount.getBalance(), "$")
acount.setBalance(1000)
print(acount.getBalance(), "$")

