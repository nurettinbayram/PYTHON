# Given an integer array nums and an integer val, remove all occurrences of val in nums
# in-place. The order of the elements may be changed. Then return the number of elements
# in nums which are not equal to val.
# Consider the number of elements in nums which are not equal to val be k, to get accepted,
# you need to do the following things:
# Change the array nums such that the first k elements of nums contain the elements which are
# not equal to val. The remaining elements of nums are not important as well as the size of nums.
# Return k.
# Input: nums = [0,1,2,2,3,0,4,2], val = 2
# Output: 5, nums = [0,1,4,0,3,_,_,_]
from typing import List

nums = [0,1,2,2,3,0,4,2]
val = 2

def removeElement(nums, val):
    arr =[]
    for num in range(0, len(nums)):
        if nums[num] == val:
            nums[num] = "_"
            arr.append(nums[num])
        else:
            continue
    for i in range(0, len(arr)):
        nums.remove(arr[0])
    print(nums)
    print(arr)

    return len(nums)

print(removeElement(nums, val))



# II.yol

def removeElement1(nums, val) :
    index = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[index] = nums[i]
            index += 1
    return index

# III. yol
def removeElement2(nums: List[int], val: int) -> int:
    while val in nums:
        nums.remove(val)
    return len(nums)

print(removeElement2(nums,val))