#https://www.youtube.com/watch?v=5WZl3MMT0Eg&list=PLot-Xpze53lfQmTEztbgdp8ALEoydvnRQ&index=3

class Solution(object):
    def maxSubArr(self, l:list[int])->int:
        maxSub = l[0]
        curSum = 0

        for n in l:
            if curSum<0:
                curSum=0
            curSum+=n
            maxSub = max(maxSub,curSum)
        return maxSub

s = Solution()
print(s.maxSubArr([-2,1,-3,4,-1,2,1,-5,4]))