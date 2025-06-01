from csv import excel
from typing import final

try:
    a = 5
    # b = e
    # b=0
    b='5d'
    # b =4
    print(a/b)
except ZeroDivisionError:
    print("b sifir olamaz.")
except NameError:
    print("tanimlanmayan b degeri")
except TypeError:
    print("verilerin tipleri uyumlu olmalidir")
except IndentationError:
    print("indent kontrolu")
else:
    print("else blogu except calismadiginda calisir.")
finally:
    print("Finally block Her zaman calisir.")

print("exception sonrasi codlar.") # exception sonrasi kodlar elbette calisiyor
                                      # exception olmadan yakalanan hatadan sonra ki kodlar calistirilmaz.