
##!-----------------------------------------MODULE----------------------------------------------
#? PROGRAMI BELLI BENZER ISLERI PARCALARA AYIRARAK KONTROL EDEBILIR VE DAHA RAHAT YONETEBILIRIZ
#* BU MODULLER BIR ARAYA GETILEREK KUTUPHANE OLUSTURULABILIR VE PYTHON RESMI KUTUPHANESI ----pypi.org----
#* import math diyerek math kutuphanesini projemize dahil etmis oluruz math ve buna benzer moduller python programi ile birlikte gelir



#!-----------------------------------------MATH MODULE----------------------------------------------
#*-----------------Dahil Etme yontem 1------------------
#? import math  # projeye math modulu dahil edildi

value = dir(math) #? math modulundeki butun bilesenleri FONKSIYONLARI value degiskenine atadik
print(value) # burada math taki butun fonksiyonlara erisip gosterir 

value = help(math) #? math icindeki fonksiyonlarin tanitimini yapar
print(value)

value = help(math.factorial)
print(value)

#*-----------------Dahil Etme yontem 2------------------
#? import math as islem #? math islem olarak calisir

value = islem.floor(40.36)
print(value)
value = islem.sqrt(36)
print(value)


#*-----------------Dahil Etme yontem 3------------------
from math import * #?bu durumdada math kutuphanesinin hepsini dahil eder
#? artik math objesi seklinde erismemiz gerekmiyor fonksiyonu dogrudan yazabiliriz

value = factorial(5)
print(value)

value = sqrt(25)
print(value)

#*-----------------Dahil Etme yontem 4------------------
from math import factorial, sqrt #? math kutuphanesinden factorial ve sqrt metodunu dahil eder
value = factorial(24)
print(value)

#!-----------------------------------------RANDOM MODULE----------------------------------------------
import random

result = dir(random)
result = help(random)

result = random.random() # 0.0-1.0
result = random.random()*100 # 1.0 - 100.0
result = random.uniform(0, 10) # 0.0 - 10.0
result = int(random.uniform(10, 100)) # int tamsayisi seklinde elde edilir
result = random.randint(1,1000)

#? -------------------Zar Atma Uygulamasi-------------------------------
zar1 = ["bir", "iki", "üç", "dört", "beş", "altı"]
zar2 = ["bir", "iki", "üç", "dört", "beş", "altı"]
print(f"Zar Numarasi: {zar1[random.randint(0,5)]}, {zar2[random.randint(0,5)]}")


#? -------------------Kumar Uygulamasi-------------------------------

fruits = ["Banana(x0)", "Cerry(x2)", "Pech(x0)", "Kivi(x1)", "Orenge(x2)", "Apple(x0)", "Mango(x5)", "BONUS(x10)"]
#print(f"{random.choice(fruits)} {random.choice(fruits)} {random.choice(fruits)}")
print(f"{random.sample(fruits, 3)}")
 

? -------------------Kendi Modulumuzu Olusturup Cagirma Islemi---------------
import MyModule #* MyModule adinda bir modul olusturduk ve buradan dosyamiza dahil ediyoruz

print(help(MyModule)) #* modul hakkindaki bilgiyi yansitir
print(help(MyModule.func)) #* modul icindeki func fonksiyonu  hakkindaki bilgiyi yansitir
result = MyModule.number
result = MyModule.numbers
result = MyModule.person["name"]
result = MyModule.person["age"]
p = MyModule.Person()#* class cagirimi
p.speak()

print(result)


