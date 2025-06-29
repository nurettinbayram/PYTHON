'''
bu modul hakkindaki bilgilendieme yazisidir
'''

print("Modul ekleme ve olusturma isleminiz basarili")#* bu kisim root seviyesinde oldugu icin modul import edilir edilmez bu kisim calisabilir 
number =10

numbers =[1,2,3,4]

person ={
    "name": "ali",
    "age" : "25",
    "city" : "istanbul",
}

def func(x):
    '''
    modulun fonksiyonu hakkindaki bilgilendirme yazisi
    '''
    print(f"x: {x}")
    
class Person:
    def speak(self):
        print("I am speaking...")