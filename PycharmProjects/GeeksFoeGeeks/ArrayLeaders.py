# You are given an array arr of positive integers. Your task is to find all the leaders in the array.
# An element is considered a leader if it is greater than or equal to all elements to its right.
# The rightmost element is always a leader.

arr = [16, 17, 4, 3, 5, 2]
li =[]

for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        if arr[i] >= arr[j]:
            if j == len(arr)-1 :
                li.append(arr[i])
            continue
        else:
            break
li.append(arr[len(arr)-1])
print(li)



