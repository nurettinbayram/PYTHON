# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# An input string is valid if:
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.


def isValid(s: str) -> bool:
    # Yığın: Açılış parantezlerini burada tutacağız
    stack = []

    # Kapanış parantezlerinin eşleşeceği açılış parantezlerini belirleyen sözlük
    bracket_map = {')': '(', '}': '{', ']': '['}

    # Diziyi baştan sona tarıyoruz
    for char in s:
        if char in bracket_map:  # Eğer karakter bir kapanış paranteziyse
            # Yığından en son eklenen açılış parantezini çıkarıyoruz
            top_element = stack.pop() if stack else '#'

            # Eğer açılış parantezi ile kapanış parantezi eşleşmiyorsa False döndür
            if bracket_map[char] != top_element:
                return False
        else:  # Eğer karakter bir açılış paranteziyse
            stack.append(char)  # Yığına ekle

    # Yığın boşsa, tüm açılış parantezlerinin doğru şekilde kapandığını anlarız
    return not stack

# Test Durumları
print(isValid("()"))  # True -> Her iki parantez eşleşiyor.
print(isValid("()[]{}"))  # True -> Her üç parantez de doğru sırada eşleşiyor.
print(isValid("(]"))  # False -> Parantezler eşleşmiyor.
print(isValid("([)]"))  # False -> Yanlış sırada kapanış parantezleri var.
print(isValid("{[]}"))  # True -> Parantezler doğru sırada eşleşiyor.

print('------------------------------------')
m =[1]
print(m.pop() if m else "y") #dizi bosmu degilmi