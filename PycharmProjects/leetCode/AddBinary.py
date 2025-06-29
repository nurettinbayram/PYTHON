# Input: a = "11", b = "1"
# Output: "100"
a = "1110"
b = "1"

def addBinary(a :str, b: str)->str:
    return str((bin(int(a,2)+int(b,2))).split("b")[-1])

print(addBinary(a,b))

