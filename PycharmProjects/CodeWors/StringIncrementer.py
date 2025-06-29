# Your job is to write a function which increments a string, to create a new string.
# If the string already ends with a number, the number should be incremented by 1.
# If the string does not end with a number. the number 1 should be appended to the new string.
# foo -> foo1
# foobar23 -> foobar24

#https://www.codewars.com/kata/54a91a4883a7de5d7800009c/train/python

import re


def increment_string(s):
    # Sayıyla biten kısmı ayırıyoruz
    match = re.search(r'(\d*)$', s)
    num_str = match.group(1)

    # Eğer sayı yoksa (s boş ya da sonunda sayı yoksa)
    if not num_str:
        return s + '1'

    # Sayı varsa:
    num_len = len(num_str)  # Örneğin "009" → 3
    incremented = str(int(num_str) + 1).zfill(num_len)

    return s[:-num_len] + incremented


print(increment_string("f25oo099"))
print("4".zfill(3))
# II yol
# def increment_string(strng):
#     head = strng.rstrip('0123456789')
#     tail = strng[len(head):]
#     if tail == "": return strng+"1"
#     return head + str(int(tail) + 1).zfill(len(tail))


