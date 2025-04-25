# "(){}[]"   =>  True
# "([{}])"   =>  True
# "(}"       =>  False

# def valid_braces(s):
#     pairs = {")":"(" ,"}":"{","]":"["}
#     stack =[]
#     for char in s:
#         if char in "({[":
#             stack.append(char)
#         elif char in ")]}":
#             if not stack or pairs[char] != stack[-1]:
#                 return False
#             stack.pop()
#     return not stack

## II. yol
def validBraces(s):
  while '{}' in s or '()' in s or '[]' in s:
      s=s.replace('{}','')
      s=s.replace('[]','')
      s=s.replace('()','')
  return s==''


#print(valid_braces("()[]["))
print(validBraces("{[({})]{{[]()()}}()}[])"))