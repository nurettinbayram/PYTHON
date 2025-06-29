# 1. yol
"""
import math
result = math.ceil(0.2)
result = math.sqrt(9)
result = math.factorial(7)
result = math.sin(45)
result = math.cos(45)
result = math.floor(45.6)
result = math.degrees(-4)
"""

# 2. yol
"""
from math import * #bu kisimda mosul ismi cagirilmadan methodlar yazilabilir
result = factorial(4)
result = floor(4.5)
"""

# 3. yol
"""
from math import  sqrt, ceil
result = sqrt(7)
result = ceil(4.5)
"""

# 4. yol
"""
import math as calculate
result = calculate.factorial(5)
result = calculate.cos(14)
print(result)
"""

import random
import string
import math

def sifre_uret(uzunluk, harf=True, rakam=True, sembol=True):
    karakter_havuzu = ""

    if harf:
        karakter_havuzu += string.ascii_letters  # a-z + A-Z

    if rakam:
        karakter_havuzu += string.digits  # 0-9

    if sembol:
        karakter_havuzu += string.punctuation  # !@#...

    if not karakter_havuzu:
        return "Hiçbir karakter türü seçilmedi."

    sifre = "".join(random.choice(karakter_havuzu) for _ in range(uzunluk))
    return sifre


# Kullanıcıdan bilgi al
print("🔐 Şifre Oluşturucu")
uzunluk = int(input("Şifre uzunluğu kaç karakter olsun? "))
harf = input("Harf olsun mu? (E/h): ").lower() != 'h'
rakam = input("Rakam olsun mu? (E/h): ").lower() != 'h'
sembol = input("Sembol olsun mu? (E/h): ").lower() != 'h'

sifre = sifre_uret(uzunluk, harf, rakam, sembol)
print(f"\n🎯 Oluşturulan Şifre: {sifre}")


