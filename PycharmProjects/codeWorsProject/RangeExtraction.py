# A format for expressing an ordered list of integers is to use a comma separated list
# of either  individual integers or a range of integers denoted by the starting integer
# separated from the end integer in the range by a dash, '-'. The range includes all
# integers in the interval including both endpoints. It is not considered a range unless
# it spans at least 3 numbers. For example "12,13,15-17"
# Complete the solution so that it takes a list of integers in increasing order and returns
# a correctly formatted string in the range format.
# Girdi: [1, 2, 3, 5, 6, 7, 9]
# Çıktı: "1-3,5-7,9"
#
# Girdi: [12,13,14,16,18,19,20,21]
# Çıktı: "12-14,16,18-21"
#https://www.codewars.com/kata/51ba717bb08c1cd60f00002f/train/python

def solution(lst):
    result = []
    i = 0
    while i < len(lst):
        start = i
        # Ardışık olanları bul
        while i + 1 < len(lst) and lst[i + 1] == lst[i] + 1:
            i += 1
        if i - start >= 2:
            # En az 3 sayı varsa range formatında yaz
            result.append(f"{lst[start]}-{lst[i]}")
        else:
            # Değilse aralığı tek tek yaz
            result.extend(map(str, lst[start:i + 1]))
        i += 1
    return ",".join(result)




lt = [12,13,14,16,18,19,20,21]
# Çıktı: "12-14,16,18-21"
print(solution(lt))







