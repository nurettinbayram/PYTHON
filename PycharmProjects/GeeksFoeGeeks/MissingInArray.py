arr = [2]
arr.sort()
print(arr)
if arr[0] != 1:
    print(1)
if len(arr) ==1:
    print(2)
for i in range(len(arr)-1):
    if (arr[i+1]) != (arr[i]+1):
        print(arr[i] +1)

