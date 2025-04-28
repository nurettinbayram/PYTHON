# import string
# alphabet = list(string.ascii_lowercase) //alfabet i dinamik kullanmak
from networkx.classes import is_empty
from unicodedata import numeric

alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]
cont ="yes"


def encodeOrDecode(text, shift, task):
    if task == "decode":
        shift*=(-1)
    newtext=""
    for i in text:
        if i in alphabet:
            indx = alphabet.index(i) +shift
            indx %=26 # 26 harf bulundugundan mod alip sayinin  disina cikmasini engelledik
            newtext += alphabet[indx]
        else:
            newtext +=i
    print(f"-----------------\noriginal text is {text}\nchanged text is {newtext}\n---------------")


while cont == "yes":
    porpes = input("enter encode or decode? ")
    text =  input("enter your text? ").lower()
    shift =  int(input("enter your shift? (it only numbers)"))
    print(porpes)
    if (porpes=="encode" or porpes == "decode") and not text=="":
        encodeOrDecode(text, shift, porpes)

    else:
        print("check yor text or your purpuse")

    cont = input("re-start ( yes or no ) ? ").lower()

