str = "AAAABBBCCDAABBBCDCE"
li = []
first = str[0]
li.append(first)
print(len(str))
for i in range(len(str)-1):
    if(str[i] != str[i+1]):
        li.append(str[i+1])
print(li)

for ch in str: ## strin for
    print(ch)

# II. Solution
result = []
prev = ""
for char in str[0:]:
    if char != prev:
        result.append(char)
        prev = char
print(result)