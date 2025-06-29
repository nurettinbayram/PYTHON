import os

# dosya var mi yok mu kontrol eder?
if os.path.exists("test.txt"):
    print("dosya mevcut zaten!!!")
else:
    print("dosya bulunamadi!!!")
    open("test.txt", "w").write("dosya yeniden olusturuldu")
    print("dosya olusturuldu...")

#dosya sile islemi!
# os.remove("test.txt") # dosya bulunamazsa hata verir


# gecerli calisma dizinini verir
print(os.getcwd())

# gecerli dizindeki tum dosya ve klasorleri liste halinde verir
print(os.listdir())

# yada belirtilen dizinin altindaki dosya ve klasorleri siralar
print(os.listdir("C:/Users/fakha/DERSLER"))