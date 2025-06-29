class InvalidNoteException(Exception):
    def __init__(self, girilenNot):
        self.girilenNot = girilenNot
        self.msg = f"Girilen NOT negatif deger olamaz...girdiginiz not {self.girilenNot}"
        super().__init__(self.msg)

class TooHighNoteException(Exception):
    def __init__(self, girilenNot):
        self.girilenNot = girilenNot
        self.msg = f"Girilen NOT 100 den buyuk deger olamaz...girdiginiz not {self.girilenNot}"
        super().__init__(self.msg)

def enter_grade(result):
    try:
        result = int(result)  # Önce string bile olsa integer'a çevirmeye çalış
    except ValueError:
        raise TypeError(f"Sadece sayısal değer girilmelidir. Girdiğiniz değer: '{result}'")

    if result < 0:
        raise InvalidNoteException(result)
    elif result>100:
        raise TooHighNoteException(result)
    else:
        print(f"0 ile 100 arasindda not girdiniz notunuz : {result} tur.")

try:
    #enter_grade(101)
    #enter_grade("-10")
    enter_grade("sa")
    #enter_grade(-10)

except InvalidNoteException as e:
    print(f"Hata yakalandi: {e}")
except TooHighNoteException as e:
    print(f"Hata yakalandi: {e}")
except TypeError as e:
    print(f"Hata yakalandi: {e}")

