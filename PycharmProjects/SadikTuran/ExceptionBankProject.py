# ------------------- Özel exception sınıfımız ---------------------
class InsufficientBalanceException(Exception):
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        self.msg = f"Yetersiz bakiye! Çekmek istediğiniz tutar: {amount}, mevcut bakiye: {balance}"
        super().__init__(self.msg)

# ------------------- Banka Hesabı sınıfı --------------------------
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Yatırılan miktar pozitif olmalıdır.")
        self.balance += amount
        print(f"{amount} TL yatırıldı. Yeni bakiye: {self.balance} TL")

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Çekilecek miktar pozitif olmalıdır.")
        if amount > self.balance:
            raise InsufficientBalanceException(self.balance, amount)
        self.balance -= amount
        print(f"{amount} TL çekildi. Kalan bakiye: {self.balance} TL")

# ------------------- Kullanım ve hata yönetimi ---------------------
try:
    account = BankAccount("Nurettin", 1000)
    account.deposit(500)
    account.withdraw(200)
    account.withdraw(1500)  # Bu satır exception fırlatacak
except InsufficientBalanceException as e:
    print(f"İŞLEM HATASI: {e}")
except ValueError as e:
    print(f"GİRİŞ HATASI: {e}")
