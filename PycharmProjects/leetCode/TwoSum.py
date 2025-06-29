

class Solution(object):
    def twoSum(self, nums:list[int], target:int)->list[int]:
        prewMap ={}

        for i, item in enumerate(nums):
            diff = target-item
            if diff in prewMap:
                return [prewMap[diff], i]
            prewMap[item] = i
        return []

s = Solution()
print(s.twoSum([2,11,15,20,26,], 22))
