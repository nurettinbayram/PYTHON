arr = ["flower","flow","flight"]
arr.sort()
firstItem = arr[0]
lastItem = arr[len(arr)-1]
indx = 0
while indx < len(firstItem) and indx < len(lastItem):
    if firstItem[indx] == lastItem[indx]:
        print(firstItem[indx])
        indx+=1
    else:
        break

