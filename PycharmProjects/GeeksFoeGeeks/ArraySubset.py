#Given two arrays a[] and b[], your task is to determine whether b[] is a subset of a[].

a = [11, 7, 1, 13, 21, 3, 7, 3]
b = [11, 3, 7, 2, 1, 7, 4]
def isSubset(a, b):
    freq = {}
    for num in a:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    for num in b:
        if num not in freq or freq[num] == 0:
            return 0
        freq[num] -= 1
    return 1

print(isSubset(a,b))