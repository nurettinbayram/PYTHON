from abc import ABC, abstractmethod

# ⛔️ Abstraction + Interface
# BankaHesabi soyut sınıfı, farklı hesap türleri için ortak davranışları tanımlar
class BankaHesabi(ABC):
    def __init__(self, hesap_sahibi, bakiye=0):
        self._hesap_sahibi = hesap_sahibi    # encapsulation (protected erişim)
        self._bakiye = bakiye                # encapsulation

    @abstractmethod
    def hesap_turu(self):
        # Her hesap türü kendi adını verecek
        pass

    def para_yatir(self, miktar):
        self._bakiye += miktar
        print(f"{miktar}₺ yatırıldı. Yeni bakiye: {self._bakiye}₺")

    def para_cek(self, miktar):
        if miktar <= self._bakiye:
            self._bakiye -= miktar
            print(f"{miktar}₺ çekildi. Yeni bakiye: {self._bakiye}₺")
        else:
            print("Yetersiz bakiye.")

    def bakiye_goster(self):
        print(f"{self._hesap_sahibi} adlı kişinin bakiyesi: {self._bakiye}₺")


# ✅ Inheritance (Kalıtım): Vadesiz ve Vadeli hesaplar BankaHesabi’ndan türemiştir
class VadesizHesap(BankaHesabi):
    def hesap_turu(self):
        return "Vadesiz Hesap"


class VadeliHesap(BankaHesabi):
    def hesap_turu(self):
        return "Vadeli Hesap"


# ✅ Polymorphism: Aynı metot farklı şekillerde çalışıyor
def hesap_bilgisi_goster(hesap: BankaHesabi): # hesap ->  BankaHesabi turunde bir obje bekliyor
    print(f"Hesap Türü: {hesap.hesap_turu()}")
    hesap.bakiye_goster()


# 💡 Kullanım:
hesap1 = VadesizHesap("Ali", 1000)
hesap2 = VadeliHesap("Zeynep", 2000)

hesap1.para_yatir(500)
hesap1.para_cek(200)

hesap2.para_yatir(1000)
hesap2.para_cek(500)

# ✅ Polymorphic fonksiyon çağrısı
hesap_bilgisi_goster(hesap1)
hesap_bilgisi_goster(hesap2)
