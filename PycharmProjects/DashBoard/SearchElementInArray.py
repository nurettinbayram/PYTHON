# You are given an array A  of size  N and an element X. Your task is to find whether the array
# A contains the element X or not.

"""
N, X = map(int, input().split())
A = list(map(int, input().split()))

if X in A:
    print("YES")
else:
    print("NO")
"""

# İlk satır şunları içerecektir: T, test vakalarının sayısı. Daha sonra test vakaları gelir.
# Her test durumundaki ilk satır bir tam sayı içerir,N. Aşağıdaki satır şunları içerir:
# N boşlukla ayrılmış tam sayılar: her dağın yüksekliği.
# https://www.codechef.com/practice/course/arrays/ARRAYS/problems/UWCOI20A

T = int(input())


while T>0:
    N = int(input())
    A = list(map(int, input().split()))
    print(max(A))
    T-=1