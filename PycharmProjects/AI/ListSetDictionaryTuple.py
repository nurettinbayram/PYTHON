# setler arasindaki calisma

print("---------------setler arasindaki calisma-------------")
a = {1, 2, 3}
b = {3, 4, 5}

print(a.union(b))
print(a.intersection(b))
print(a.difference(b))
print(a.symmetric_difference(b))

print(a|b)
print(a&b)
print(a^b)
print(a-b)