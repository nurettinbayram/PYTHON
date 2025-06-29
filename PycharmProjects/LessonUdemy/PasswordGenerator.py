import string
import random

lettersArray = list(string.ascii_letters)
symbolsArray = list(string.punctuation)
numbersArray = list(string.digits)
complexArray = []


def selectPasswordChar(arr, c):
    for i in range(c):
        complexArray.append(random.choice(arr))

print("Welcome to the PyPassword Generator!")
letters = int(input("How many letters would you like in your password?"))
symbols= int(input("How many symbols would you like?"))
numbers =int(input("How many numbers would you like?"))

selectPasswordChar(lettersArray, letters)
selectPasswordChar(symbolsArray, symbols)
selectPasswordChar(numbersArray, numbers)

print(''.join(complexArray))
random.shuffle(complexArray) # elimizde olan listeyi rastgele sekilde karistirip getrir
print(''.join(complexArray))


