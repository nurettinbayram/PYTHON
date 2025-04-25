
#! ------------------HATA YONETIMI------------------------------
 #print(a)       => #NameError: name 'a' is not defined
 #int("1a2")     => #ValueError: invalid literal for int() with base 10: '1a2'
 #print(10/0)    => #ZeroDivisionError: division by zero
 #print("denem"e)=> #SyntaxError: invalid syntax. Perhaps you forgot a comma?
 #print("deneme")=> #IndentationError: unexpected indent #!bu istenilen duzenden cikilmasi hatasi girinti hatasi


#! ------------------Gelen Hatalari Ele Alalim--------------------

try:
    x = int(input("X: "))
    y = int(input("Y: "))
    print(x/y)
except ZeroDivisionError:#(ZeroDivisionError,ValueError) seklinde bir exset altindada hatalarin kodlari yazilabilir
    print("y degeri icin sifir girmemelisin")
except ValueError:
    print("x ve y icin sayisal deger girmelisiniz")

#!----------------------------------------------------
try:
    x = int(input("X: "))
    y = int(input("Y: "))
    print(x/y)
except (ZeroDivisionError, ValueError):
    print("y degeri icin sifir girmemelisin && x ve y icin sayisal deger girmelisiniz")


#!----------------------------------------------------
try:
    x = int(input("X: "))
    y = int(input("Y: "))
    print(x/y)
except (ZeroDivisionError, ValueError) as e:
    print("y degeri icin sifir girmemelisin && x ve y icin sayisal deger girmelisiniz\n" ,e)#* e ile hata turunu yazdirilir

#!----------------------------------------------------
try:
    x = int(input("X: "))
    y = int(input("Y: "))
    print(x/y)
except:
    print("Hatali bilgi girdiniz")#* 

#!----------------------------------------------------
try:
    x = int(input("X: "))
    y = int(input("Y: "))
    print(x/y)
except:
    print("Hatali bilgi girdiniz") 
else:
    print("hersey yolunda")#! kodlar doru calismasi durumunda calisir

#!----------------------------------------------------
try:
    x = int(input("X: "))
    y = int(input("Y: "))
    print(x/y)
except Exception as ex:
    print("Hatali bilgi girdiniz\n=>", ex) 
else:
    print("hersey yolunda")#! kodlar doru calismasi durumunda calisir
finally:
    print("her zaman calisan bir block")

#! ---------------------Exception Firlatma--------------------
x = 10

if x>5:
    raise Exception("x 5 ten buyuk olamaz.")#consola yazdirir


#! -------------------------Parola Control Uygulamasi-----------------------------

def check_password(psw):
    import re # regular excpration dahil ettik
    #elif not kullanimina dikkat
    if len(psw)<8:
        raise Exception("Parola en az 8 karakter olmalidir")
    elif not re.search("[a-z]", psw):
        raise Exception("Parola kucuk harf icermelidir")
    elif not re.search("[A-Z]", psw):
        raise Exception("Parola buyuk harf icermelidir")
    elif not re.search("[0-9]", psw):
        raise Exception("Parola rakam icermelidir")
    elif not re.search("[_@$]", psw):
        raise Exception("Parola alfa numeric karakter harf icermelidir")
    elif re.search("\\s", psw): #bosluk karakteri ozel karakterlerin onune iki tane ters slash yada elif re.search(r"\s", psw):  # 'r' eklenerek raw string yapıldı
        raise Exception("Parola bosluk karakter icermemelidir")
    else:
        print("Parolaniz olusturuldu ", psw)
    
        
password = "45645455wD@"

try:
    check_password(password)
except Exception as ex:
    print(ex)
else:
    print("Parolaniz gecerli.") #except calismazsa bu calisir
finally:
    print("validation tamamlandi")# her zaman  calisir dikkat

#! ----------------------Sorular----------------------------
#* 1- listedeki sayisal degerleri bulunuz
list = ["1", "2", "5s", "sd", "45", "56az"]

for i in list:
    try:
        result = int(i)
        print(result)
    except ValueError:
        continue

#* 2- kullanici q degeri girmedikce alinan degerin sayi olup olmadigini kontrol eder


while True:
    x = input("bir sayi giriniz : ")
    if x=="q":
        break
    else:
        try:
            int(x)
            print(x , "bir sayidir")
        except ValueError:
            print("lutfen sayi girdiginizden emin olun")

#* 3. soru: girilen parolanin turkce karakter icermemeli durumunu kontrol etme

def checkPassword(parola):
    turkceKarakterler= "ğĞçÇşŞüÜöÖıİ"
    for i in parola:
        if i in turkceKarakterler:
            raise TypeError("Parola turkce karakter icermemelidir")
        else:
            pass
        
    print("gecerli parola")
    
parola = input("parola giriniz: ")
try:
    checkPassword(parola)
except TabError as e:
    print('parola gecersiz', e)



        
        
    
