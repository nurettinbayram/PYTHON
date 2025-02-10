#------------------------------listeler--------------------------------------
# message="hello there. my name is nurettin".split()#split bosluklara gore ayirdi ve listeye cevirdi
# print(message[2])

# mylist = [1,2,3,4]
# mylist =['bir', 2, True, 5.6] #listeler farkli turden degerler tutabilir
# print(mylist)

# list1 = ['one', 'two', 'three']
# list2 = ['four', 'five', 'six']
# list3 = list1+list2 #listeler toplanabilir
# print(list3)
# print(len(list3))

# userA = ['nurettin', 45]
# userB = ['cano', 78]
# print(userA)
# print(userB)
# users = userA + userB# tek bir liste halinde gorulur
# print(users)

# userA1 = ['faih', 45]
# userB1 = ['kenan', 78]
# print(userA1)
# print(userB1)
# users1 = [userA1, userB1]# araya arti isaredi degilde vurgul ve koseli parantezlerde olunca iki ayri liste ayni anda birlestirilir 
# print(users1)
# print(users1[0]) #burada [0] index [fatih, 45] olarak karsimiza cikar
# print(users1[0][0])# buradada sonuc fatihtir


#------------------ornekler---------------------
# list =["bmw", "mercedes", "opel", "mazda"]
# print(len(list))
# print(list[0])
# print(list[(len(list)-1)])
# list[-1]= "scoda"
# print(list)
# value='bmw' in list # bir degerin listede olup olmadigini sorgular
# print('evet' if value else 'hayir') #pythone if else kisa yazilimi
# print(list[-2])
# listx=list[0:2] #listenin ilk iki elemani gelir
# print(listx)
# list[2:] = ['toyota', 'reno']# listenin 2-3 elemanina yeni eleman ekleme
# print(list)
# print(list + ['audi', 'nissan']) # listeye iki eleman daha ekleme
# print(list)
# #list.pop() #son elemani cikarma metodu
# del list[-2] #istenilen degerdeki elemanlari siler
# print(list)
# list.reverse()
# print(list)
# list[::-1] #liste elemanlarini tersten yazmanin baska yolu
# print(list)

# studentA = ['yigit', 'bilgin', 2010, (70,60,50)]
# studentB = ['serap', 'kisaparmak', 2010, (70,60,50)]
# studentC = ['ahmet', 'kaya', 2001, (30,70,40)]
# students = studentA+studentB+studentC #yikaridaki ogrencileri birlestirme islemi
# print(students)
# result= f"{studentA[0]} {studentA[1]} {2025-studentA[2]} yasinda ve not ortalamasi {(studentA[3][0]+studentA[3][1]+studentA[3][2])/3}"
# print(result)

#-----------------DERS3.14 LISTELER--------------------------------
# numbers = [1,22,3,14,5,46,7,80,10]
# latters = ['a','b','a','d','a','k','o','z']

# val = min(numbers)
# print(val)
# val = max(numbers)
# print(val)
# val = min(latters)
# print(val)
# val = max(latters)
# print(val)
# numbers.append(45) #son elemandan sonra ekleme yapar
# print(numbers)
# numbers.append(485)
# print(numbers)
# numbers.insert(3, 787)#istenilen index yerine yazdirma
# print(numbers)
# numbers.pop()#son elemani siler
# print(numbers)
# numbers.pop(2)#2. ndekteki elemani siler
# print(numbers)
# numbers.pop(-1)#son elemani siler 
# print(numbers)
# numbers.remove(787)#dizideki listedeki belirtilen numara  silinir
# print(numbers)
# numbers.sort()# kucukten buyuge siralar
# print(numbers)
# latters.sort()#alfabetik olarak siralar
# print(latters)
# latters.reverse()
# print(latters)
# print(latters.count('a'))#kac adet a bulundugunu sayar
# print(latters.count('d'))
# print(latters.count('p'))
# latters.clear()#listenin icini bosaltir
# print(latters)

#----------------------DERS3.15 LISTE ORNEKLERI------------------------------
# name = ['ali', 'yagmur', 'hakan', 'deniz']
# years = [1998, 2000, 1998, 1987]

# name.append('cenk')
# print(name)
# name.insert(0, 'sena')
# print(name)
# den=name.index('deniz')
# print(den)
# name.remove('deniz')
# print(name)
# al= 'ali' in name
# print(al)
# name.reverse()
# print(name)
# name.sort()
# print(name)
# str = "haci,can"
# str = str.split(',')
# print(str)
# x=max(years)
# print(x)
# cont = years.count(1998)
# print(cont)
# years.clear()
# print(years)

# markalar =[]

# marka = input("marka: ")
# markalar.append(marka)
# marka = input("marka: ")
# markalar.append(marka)
# marka = input("marka: ")
# markalar.append(marka)

# print(markalar)

#------------------DERS3.16 DICTIONARY------------------
# persen= {
#     'nurettin':{
#         'age':25,
#         'email':'nurettin@gmail.com',
#         'rol':['user', 'admin'],
#         'adress': 'New York',
#         'phone':'144587'
#     },
#     'cinar':{
#         'age':2,
#         'email':'cinar@gmail.com',
#         'rol':['user'],
#         'adress': ' York',
#         'phone':'143647'
#     }
# }

# print(persen['nurettin'])
# print(persen['nurettin']['adress'])
# print(persen['nurettin']['rol'][0])
# print(persen['cinar']['email'])

#------------------DERS3.16 DICTIONARY EXEMPLE------------------

# ogrenciler= {
#     '120':{
#         'ad':'ali',
#         'soyad':'yilma',
#         'telefon':'252 525 15 12'
#     },
#     '125':{
#         'ad':'can',
#         'soyad':'korkmaz',
#         'telefon':'457 725 15 12'
#     },
#     '128':{
#         'ad':'volkan',
#         'soyad':'yukselen',
#         'telefon':'111 665 15 12'
#     },
# }

# numara= input("ogrenci numarasini giriniz: ")
# ad= input("ogrenci adini giriniz: ")
# soyad= input("ogrenci soyadini giriniz: ")
# telefon= input("ogrenci telefonunu giriniz: ")

#yeni bir ogrenci ekleme inputtan alinan degerlerle 
# ogrenciler[numara]={
#     'ad':ad,
#     'soyad':soyad,
#     'yelefon': telefon
#     }
#yukarinin alternatifi olarak Update metoduda kullanilabilir
# ogrenciler.update({
#     numara:{
#      'ad':ad,
#      'soyad':soyad,
#      'telefon': telefon
#      }
#      })
# print(ogrenciler)

# #ogrenci numarasini imputtan girip sonucu ogrenci bilgilerini alir
# ogrNo = input('ogrenci numarasini giriniz: ')
# ogrenci = ogrenciler[ogrNo]
# print(f'Aradiginiz {ogrNo} nolu ogrencinin adi : {ogrenci['ad']} soyadi: {ogrenci['soyad']} ve telefon numarasi: {ogrenci['telefon']}')


#----------------------METHOD--------------
# methodlar classlarin icerisinde tanimlanir


#----------------------FUNCTION--------------
#kendi baslarina olusturulur

# def sayHello(name = 'user'):#burada name = user ifadesi defoult olan ifadedir bu sebepten eger cagrilan fonksiyonda herhangi bir isim bulunmazsa user ismi yazilir
#     print('Hello ' + name)
    
# sayHello('ali')
# sayHello('cano')
# sayHello()

# def sayHello1(name = 'user'):
#     return 'Hello ' +name  # return ifadesi ile fonksiyon deger dondurur

# msg=sayHello1('nuretti') #fonksiyondan donen degeri bir degiskene atayip istenilen sekilde kullanabiliriz
# print(msg)

# def total(num1=0, num2=0):#defoult degerleri 0 oldugu isin herhangi bir sayi gonderilmezse 0 degeri doner
#     '''
#     DOCSTRING : iki sayinin toplamini yapar
#     INPUT: iki sayi yollama
#     OUTPUT: sayilarin toplaminin sonucunu dondurme
#     '''
#     return num1+num2

# print(help(total))

# result = total(1,5)
# result = total()
# print(result)

# list = [1, 2, 3]
# print(help(list.index))
# print(list.index(3))

# print('---------------------------------------------------')

# def changeValueType(n):
#     n = 'ada'
    
# name = 'yigit'
# changeValueType(name) #yigit adinda name bilgisini chanceValue fonksiyonuna gonderdik ama name degerini ada ile degistiremedi cunku value tipler 
# print(name)

# def changeReferansType(m):
#     m[0] = 'istanbul'

    
# sehirler = ['ankara', 'izmir']
# changeReferansType(sehirler)# sehirler disisinin ilk elemani ankara olmasina ragmen fonksiyona gonderilince 0'inci indeksteki degeri istanbulla degistirilir cunku bu bir referan tip ifadedir
# print(sehirler)


# def add1(x, y, z=0): #burada funksiyona iki yada uc parametre gonderilebilir toplama islemi yapilir
#     return sum((x,y,z))

# print(add1(10, 20, 60))
# print(add1(10, 20))

# def add2(*params): #burada funksiyona istenildigi kadar parametre gonderilebilr parametre gonderilebilir toplama islemi yapilir buradaki tek yildizin onemi cok
#     return sum((params))

# print(add2(10, 20, 60))
# print(add2(10, 20, 30, 40, 50, 70))

# def add3(*params):
#     sum = 0
#     for n in params: #purada params tuple listesindeki elemanlari tek tek don n degiskenine ata ve dondur
#         sum = sum+ n
#     return sum

# print(add3(10, 20, 30, 40, 50, 70, 60))

# def displayUser(**args):#buradaki ** iki yildiz bize dictionary gelecegini bildirir. yani key->value args ifadesi bir dictionarydir
#     for key, value in args.items():
#         print('{} is {}'. format(key , value))

# displayUser(name = 'cinar', age= '2', city = 'istanbul')
# displayUser(name = 'ada', age= '45', city = 'sirnak', phone = '453354')
# displayUser(name = 'yigit', age= '24', city = 'new york', phone = '453354', email = 'yigit@gmail.com')

# def myFunction(a, b, c, *args, **kwargs): #buradaki degerlere bakar ilk uc siradakini noraml deger olarak atamisiz sonrakini bir tuple daha sondasinda bir dictionary bu burumda elemanlari ona gore eslestirir
#     print(a)
#     print(b)
#     print(c)
#     print(args)
#     print(kwargs)
    
# myFunction(10, 50, 30,  50, 60, key1 = 'value1', key2 ='value2')

#--------------------FONKSIYONLAR EXEMPLE------------------------

#--------------------1-EXEMPLE------------------------
#print('-----------------1-EXEMPLE------------------------------')
# def wordFunc(w, c):
#     for i in range(c): #for dongusunu bu sekilde istenilen sayida dondurebiliriz kullanimi bu sekil
#         print(w)
    
# myWord = input('yazdirmak istediginiz kelimeyi yaziniz: ')
# countity = input('yazdiginiz kelimeyi kac kere yazdirmak istediginizi belirtiniz: ')
# x = int(countity) # tur donusumu bu sekilde yapilir ve inputtan gelen her ifade sitring tipinde gelir
# wordFunc(myWord, x)
#print('-------------------2-EXEMPLE----------------------------')

#--------------------2-EXEMPLE------------------------
# def myFunc(*params):
#     for i in params:
#         myList = []
#         myList = params
#     print(myList)

# myFunc('nurettin', 29, 'sirnak', 'nina@gmail.com', 480738)

#print('-------------------3-EXEMPLE----------------------------')

#--------------------3-EXEMPLE------------------------
# def asalFunc(x ,y):
#     for sayi in range(x, y+1):
#         for i in range(2, sayi):
#             if (sayi%i == 0):
#                 break
#         else:
#             print(sayi)
                

# print("iki sayi arasindaki asal sayilari bulma islemi")
# x1 = input('birinci sayi giriniz: ')
# x2 = input('ikinci sayi giriniz: ')
# asalFunc(3, 50)

print('-------------------MAP LAMDA FILTER----------------------------')
def square(num): return num**2

numbers0 = [1,2,3,4,5]
result0 = list(map(square, numbers0)) #uradada map metodu ile dizideki elemanlara ulasabiliriz
print(result0)

for item in map(square, numbers0):#map metodu ile dizi icindeki verilere ulasabiliriz
    print(item)

numbers1 = [9,5,6,2,3,4,5]
multi = lambda num: num*num #burada lamda ile gorunmezz bir fonksiyon olusturduk bunuda multi degiskenine atadik
result1 = list(map(multi, numbers1))
print(result1)

numbers2 = [8,5,7,5,6,2,3,4,5]
result2 = list(map(lambda x: x**3, numbers2))#istenilse lamda bu sekilde de kullanilabilir
print(result2)
 

numbers3 = [8,5,7,5,6,2]
def check_even(num): return num%2==0
result3 = list(filter(check_even, numbers3))#filter ozelligi ile dizi icerisinden cift elemanlari geriye dondur
print(result3)

numbers4 = [4,9,6,8,5,7,5,6,2]
result4 = list(filter(lambda num:num%2 == 0, numbers4))# yukaridaki ornekte oldugu gibi lamda ile bu islemi yapmak fonsiyonsuz bir sekilde mumkun
print(result4)

numbers5 = [4,5,7,5,6,2]
check_even1 = lambda num:num%2 == 0
result5 = list(filter(check_even1, numbers5))# yukaridaki ornekte oldugu gibi lamda degerini check_even1 e atayip yerinde kullanabiliriz
print(result5)

