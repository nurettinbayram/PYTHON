# Input: s = "   fly me   to   the moon  "
# Output: 4
# Explanation: The last word is "moon" with length 4.

s = "   fly me   to   the moon  "
def lengthOfLastWord(s:str):
    sArr = s.split()
    return len(sArr[len(sArr)-1])

print(lengthOfLastWord(s))