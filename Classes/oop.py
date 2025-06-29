print("----------------------OOP--------------------------")

#!  Class
class Person:
    #? Class attributes
    adress = "No information"
    
    #? Constructer(yapici method)
    def __init__(self, name, year):#? buradaki self uretilen objeyi temsil ediyor
        # init metodu olusturulan her obje icin calistirilir  
        
        #? Object Attrbutes
        self.name = name #burada sag taraftaki degerler disardan gelen degerler selfin yanindaki degerler yeni olusturulan deger
        self.year = year #selfin yanindaki deger degistirilebilirbir deger o bu clas icin olusturulmus degerdir digeri ise disardan gelen initin icerisinde olan degerdir(sag traftaki deger)
        print("init Clistirildi. " + name)
        
    #?instance methods
    def intro(self):
        print("Hello There. I am "+ self.name +" I am located in "+ self.adress)
    
    #?instance methods
    def calculateAge(self):
        return 2025-self.year
        
    
#? object(instance) her obje olusturuldugunda init metodu otomatik olarak calisir
p1=Person("Nurettin", 1996)
p2=Person("Keno", 1999)
p3=Person("fati", 1992)

#?updating
p1.name = "Ahnet"
p2.year = 1990
p1.adress= "Sirnak"

#? accessing object atrtributes
print(f"p1: Name: {p1.name} year: {p1.year} adress: {p1.adress}")
print(f"p2: Name: {p2.name} year: {p2.year} adress: {p2.adress}")
print('-----------------------------------')
p1.intro()
print('-----------------------------------')
print(f"Adim: {p1.name} ve yasim: {p1.calculateAge()}")
print(f"Adim: {p2.name} ve yasim: {p2.calculateAge()}")

#!---------------------------CIRCLE EXEMPLE-----------------------
class Circle:
    #?class object attrubute
    pi = 3.14   
    
    def __init__(self, yaricap=1):# bir yaricap belirtilmezse default degeri 1 olur
        self.yaricap = yaricap
        
    #? methods
    def cevreHesapla(self):
        return 2*self.pi*self.yaricap
    
    def alanHesapla(self):
        return self.pi*(self.yaricap**2)


c1 = Circle() #yaricapi 1 olarak alinir
c2 = Circle(yaricap=5)

print(f"c1: Alan = {c1.alanHesapla()} Cevre = {c1.cevreHesapla()}")
print(f"c1: Alan = {c2.alanHesapla()} Cevre = {c2.cevreHesapla()}")

#!---------------------------INHERATANCE \\ KALITIM // MIRAS -----------------------
class Person():
    def __init__(self, fName, lName):
        self.firstName = fName
        self.lastName = lName
        print("person created")
        
    def who_am_i(self):
        print("I am a person")
        print(f"my name is : {self.firstName} and my surname is {self.lastName} ")
        
    def eat(self):
        print("i am eating")
        
class Student(Person):
    def __init__(self, firstName, lastName, number="No founded"):
        Person.__init__(self, firstName, lastName)#? burada hem kendi clasimizin init metodu hemde person classin init metodu calisir
        self.studentNumber = number
        print("Student created")
        
    def who_am_i(self): #? buradaki metod person metodunu ezdi bu duruma overriding
        print("I am student.")
        print(f"my name is : {self.firstName} and my surname is {self.lastName} my number is {self.studentNumber}")

class Teacher(Person):
    def __init__(self, fName, lName, branch="Class Teacher"):
        super().__init__(fName, lName)
        self.branch = branch
        
    def who_am_i(self):
        print(f"I am {self.firstName} {self.lastName} {self.branch} teacher")
    

person1 = Person('nurettin', 'bayram')
student1 = Student('kemal', 'molodi') #? person dan miras aldigindan dolayi otomatik olarak person u calistirir
theacher1 = Teacher('fati', 'melo')

print(person1.firstName+" "+ person1.lastName)
print(student1.firstName+" "+student1.lastName)
print('-------------------------------')
person1.who_am_i()
student1.who_am_i()
person1.eat()
student1.eat()
print(student1.studentNumber)
student2 = Student("Okan", "Akyildiz", "124578")
print(student2.firstName + " " + student2.lastName+ " " +student2.studentNumber)
print("----------------------------------")
student1.who_am_i()
teacher = Teacher("murat", "sari", "math")
teacher.who_am_i()

#!---------------------------ARAC YONETIM SISTEMI -----------------------
class MyVihicle():
    def __init__(self, brand, model, year):
        self.brand =brand
        self.model =model
        self.year =year
    
    def displayInfo(self):
        print(f"Brand : {self.brand} \nModel : {self.model} \nYear : {self.year}")
        
        
class Car(MyVihicle):
    def __init__(self,brand, model, year, doors):
        super().__init__(brand, model, year) 
        self.doors = doors
        
    def displayInfo(self):
        super().displayInfo() #? myVihicle sinifinda bu metodu calistirir ve bu kendi sinifindada buna override edilerek yeni ozellikte eklendi
        print(f"Doors : {self.doors}")
        
class Motorcycle(MyVihicle):
    def __init__(self, brand, model, year, type):
        super().__init__(brand, model, year)
        self.type = type
        
    def displayInfo(self):
        super().displayInfo()
        print(f"Motor Type : {self.type}")
        
        

vihicle1 = Car('Toyota', "Prius", 2008, 4)
vihicle1.displayInfo()        
print("------------------------------")
vihicle2 = Motorcycle('Toyota', "Yamaha MT-07", 2023, "Spor Type")
vihicle2.displayInfo()


#!---------------------------OOP HAYVANLAR ALEMI -----------------------
import random
class Hayvan():
    
    def __init__(self, isim, tur, yas):
        self.isim = isim
        self.tur = tur
        self.yas = yas
        
    def ses_cikar(self):
        print("sinifi ozellestirildi")
        
    def bilgi_goster(self):
        print(f"Hayvan ismi : {self.isim} \nHayvan turu : {self.tur} \nHayvanin yasi : {self.yas}")
        
class Kus(Hayvan):
    def __init__(self, isim, yas, sesi):
        super().__init__(isim, "Kus", yas)
        self.sesi = sesi
        
    def uc(self):
        print(f"{self.isim} kus ucuyor")
        
    def ses_cikar(self):
        print(f"{self.isim} {self.sesi} sesi cikarir")
        
class Aslan(Hayvan):
    def __init__(self, isim, yas, sesi):
        super().__init__(isim, "Aslan", yas)
        self.sesi = sesi 
    
    def avlan(self):
        print(f"{self.isim} avlanir tehlikeli bir hayvan")
        
    def ses_cikar(self):
        print(f"{self.isim} {self.sesi} sesi cikarir")#Roarrrr!
        
class Fil(Hayvan):
    def __init__(self, isim, yas, sesi):
        super().__init__(isim, "Fil", yas)
        self.sesi = sesi 
    
    def su_fiskirt(self):
        print(f"{self.isim} borusuyla su fiskirtir")
        
    def ses_cikar(self):
        print(f"{self.isim} {self.sesi} sesi cikarir")#trumpettt!
        
        
        
class HayvanatBahcesi:
    
    def __init__(self):
        self.hayvanlar=[]
        
        
    def hayvan_ekle(self, hayvan):
        self.hayvanlar.append(hayvan)
        print(f"{hayvan.isim} hayvanat bahcesini eklendi")
        
    def tumHayvanlari_goster(self):
        print("Hayvanat bahcesindeki Tum hayvanlar")
        for hayvan in self.hayvanlar:
            hayvan.bilgi_goster()
            print("------------------------------")
        
        
        

hayvanatBahcesi = HayvanatBahcesi()

marti = Kus("Martı", 2, "cicici")
aslan_kral = Aslan("Aslan Kral", 5, "girrrr")
jumbo = Fil("Jumbo", 10, "wouuu")


hayvanatBahcesi.hayvan_ekle(marti)
hayvanatBahcesi.hayvan_ekle(aslan_kral)
hayvanatBahcesi.hayvan_ekle(jumbo)

hayvanatBahcesi.tumHayvanlari_goster()

marti.uc()
aslan_kral.ses_cikar()
jumbo.su_fiskirt()


#!---------------------------OOP MAGAZA  -----------------------
from datetime import datetime
class Store:
    def __init__(self, name, owner, founded_year, catagory):
        self.name=name
        self.owner=owner
        self.founded_year=founded_year
        self.catagory=catagory
        
    def display_info(self):
        print(f"Magza Adi: {self.name} \nMagaza sahibinin adi: {self.owner} \nKurulus Yili: {self.founded_year} \nKatagori: {self.catagory}\n")
        print(f"Bu mağaza {self.years_in_business(datetime.now().year)} yıldır faaliyet göstermektedir.\n")
        
    def years_in_business(self, current_year):
        return current_year-self.founded_year
        
        
class ElectronicsStore(Store):
    def __init__(self, name, owner, founded_year, catagory, Eticaret):
        super().__init__(name, owner, founded_year, catagory)
        self.Eticaret = Eticaret
        
        
    def display_info(self):
        super().display_info()
        print(f"Eticaret islemleri {"Mevcuttur" if self.Eticaret  else "Malesef teslimat yapilmiyor"} \nBu magza elektronik urunler satar")
        
class ClothingStore(Store):
    def __init__(self, name, owner, founded_year, catagory, Eticaret):
        super().__init__(name, owner, founded_year, catagory)
        self.Eticaret = Eticaret
        
        
    def display_info(self):
        super().display_info()
        print(f"Eticaret islemleri {"Mevcuttur" if self.Eticaret  else "Malesef teslimat yapilmiyor"} \nBu magza giyim urunleri satar")
        
        
s1=Store("Gitti Gidiyor", "Nurettin Bayram", 1855, "Her sey")
s1.display_info()
e1 = ElectronicsStore("Vatan", "Mehmet Bayram", 1888, "Laptop ve Telefon", True)
e2 = ElectronicsStore("Hepsi Burada", "Mehmet Bayram", 1978, "Laptop ve Telefon", False)
e1.display_info()
e2.display_info()

#!---------------------------OOP QUIZ  -----------------------
#Question
class Question:
    def __init__(self, text, choices, answer):
        self.text = text
        self.choices = choices
        self.answer = answer
    
    def checkAnswer(self, answer):
        return self.answer==answer #?disaridan girilen cevap ile sorudaki cevabin kiyaslanmasi
    
class Quiz:
    def __init__(self, questions):
        self.questions =questions
        self.score = 0
        self.questionIndex =0
        
    def getQuestion(self):
        return self.questions[self.questionIndex]#? questions listesindeki index numarasina gore secim yapilir yani q1 q2 q3 objelerinden biri secilir
    
    def displayQuestion(self):
        question = self.getQuestion() #? burada getQuestion metodunda secilmis olan obje question degiskenine atilir
        print(f"Soru {self.questionIndex + 1}/{len(self.questions)} : {question.text}")  #? secilmis olan obje nin textine  buradan ulasilir
        
        for q in question.choices: #? question.choices dizisini gezerek q ya atar
            print("-> " + q )
            
        answer = input("Cevap : ")
        self.guess(answer)
        self.loadQuestion()
        
    def guess(self, answer):
        question = self.getQuestion()
        
        if question.checkAnswer(answer):
            self.score +=1
        self.questionIndex += 1
        
    def loadQuestion(self):
        if len(self.questions) == self.questionIndex:
            self.showScore()
        else:
            self.displayQuestion()
            
            
    def showScore(self):
        print("Score : ", self.score )
        
#!bu sekilde if else yazmadan secenekler arasinda gecis yapilir ve ne kadar az if else kullanilirsa o kadar iyi program olmus olur
q1 = Question("en iyi programlama dili hangisi?", ["C#", "Python", "Java", "JavaScript"], "JavaScript")
q2 = Question("en populer programlama dili hangisi?", ["C#", "Python", "Java", "JavaScript"], "Java")
q3 = Question("en cok kazandiran programlama dili hangisi?", ["C#", "Python", "Java", "JavaScript"], "Python")
q4 = Question("en cok kazandiran programlama dili hangisi?", ["C#", "Python", "Java", "JavaScript"], "Python")
questions = [q1,q2,q3,q4]

quiz = Quiz(questions)
quiz.displayQuestion()

