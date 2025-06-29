from abc import ABC, abstractmethod

class Hayvan(ABC):
    def __init__(self, isim):
        self._isim=isim

    @abstractmethod
    def sesCikar(self):
        pass

    @property
    def getIsim(self):
        return self._isim


class Kedi(Hayvan):
    def __init__(self, isim):
        super().__init__(isim)

    def sesCikar(self):
        return  f"Benim adım {self._isim}. Miyav!"

class Kopek(Hayvan):
    def __init__(self, isim):
        super().__init__(isim)

    def sesCikar(self):
        return f"Benim adım {self._isim}. Hav hav!"

class HayvanatBahcesiYoneticisi:
    def __init__(self, hayvan: Hayvan):
        self.hayvan = hayvan

    def hayvani_tanit(self):
        print(f"Hayvan Bilgisi -> {self.hayvan.sesCikar()}")

animals = [Kedi("Pamuk"), Kopek("Karabas"), Kopek("Simsek"), Kedi("Seker"), Kedi("Boncuk")]

for animal in animals:
    hby = HayvanatBahcesiYoneticisi(animal)
    hby.hayvani_tanit()
    print(animal.getIsim) # buradaki gatter metodu @property yapildigi icin fonksiyon gibi cagrilmaz...




