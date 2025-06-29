# Input: digits = [1,2,3]
# Output: [1,2,4]
# Explanation: The array represents the integer 123.
# Incrementing by one gives 123 + 1 = 124.
# Thus, the result should be [1,2,4].
from typing import List

digits = [1,2,3]
def plusOne(digits: List[int]) -> List[int]:
    stsd=""
    for i in digits:
        stsd +=(str(i))
    stsd = str(int(stsd)+1)
    return [int(ch) for ch in stsd]
print(plusOne(digits))




