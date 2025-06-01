"""
Input: arr[] = [2, 6, 4, 1], k = 3
Output: 11
Explanation: The different subarray sums we can get from the arrayare = [13, 12, 11, 10, 8, 6, 5, 4, 2, 1].
Where 11 is the 3rd largest.
https://www.geeksforgeeks.org/problems/k-th-largest-sum-contiguous-subarray/1
"""

arr = [-7]
k = 1

t = sum(arr)
if t>0 and len(arr)>1:
    arr.clear()
    print(t)
    k = k-1
    while t>0:
        arr.append(t)
        t-=1
if t<0  and len(arr)>1:
    arr.clear()
    print(t)
    k=-1*k
    while t<0:
        arr.append(t)
        t+=1
if len(arr)==1:
    k=0
print(arr)
print(arr[k])