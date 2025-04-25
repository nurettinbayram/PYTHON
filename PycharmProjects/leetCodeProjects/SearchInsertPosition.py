# Given a sorted array of distinct integers and a target value, return the index if the
# target is found. If not, return the index where it would be if it were inserted in order.
# You must write an algorithm with O(log n) runtime complexity.
# Input: nums = [1, 3, 5, 6], target = 5
# Output: 2
# Input: nums = [1, 3, 5, 6], target = 2
# Output: 1
from operator import index

nums = [1, 3, 5, 6]
target = 4

def searchInsert(nums, target):
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    # Target bulunamadıysa, eklenmesi gereken yer: left
    return left



print(searchInsert(nums, target))