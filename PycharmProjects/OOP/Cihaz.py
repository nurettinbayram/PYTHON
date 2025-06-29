from abc import ABC, abstractmethod


# Soyut temel sınıf (interface gibi davranır)
class Cihaz(ABC):
    @abstractmethod
    def baslat(self):
        pass

    @abstractmethod
    def durdur(self):
        pass


# Yazıcı sınıfı
class Yazici(Cihaz):

    def durdur(self):
        print("yazici durduruldu")

    def baslat(self):
        print("yazici calistirildi.")


# Tarayıcı sınıfı
class Tarayici(Cihaz):

    def baslat(self):
        print("Tarayici calistirildi!!")

    def durdur(self):
        print("Tarayici durdu!!")

# Bu sınıf farklı cihazları kullanabilir (polymorphism burada)
class AygitYoneticisi:
    def __init__(self, cihaz: Cihaz):
        self.__cihaz = cihaz  # encapsulation

    def cihazi_kullan(self):
        self.__cihaz.baslat()
        print("Cihaz çalışıyor...")
        self.__cihaz.durdur()


# Test için örnek kullanım:
y1 = Yazici()
t1 = Tarayici()

yonetici1 = AygitYoneticisi(y1)
yonetici2 = AygitYoneticisi(t1)

yonetici1.cihazi_kullan()
print("----------")
yonetici2.cihazi_kullan()
