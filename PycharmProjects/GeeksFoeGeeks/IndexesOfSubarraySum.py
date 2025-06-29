
arr = [19, 23, 15, 6, 6, 2, 28, 2]
target = 2
for i in range(len(arr)):
    sum = 0
    x=False
    sum += arr[i]
    for j in range(i, len(arr)):
        if i == j:
            sum = arr[i]

        else:
            sum =sum  + arr[j]
        x = (sum == target)
        if x:
            print (i+1, j+1)
            break
        elif sum > target:
            break
    if x:
        break