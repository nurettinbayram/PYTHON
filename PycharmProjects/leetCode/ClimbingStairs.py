# You are climbing a staircase. It takes n steps to reach the top.
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?


# I. way
'''
def climbStairs(n):
    if n <= 2:
        return n

    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 2

    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]
print(climbStairs(4))
'''

# II. way
# https://www.youtube.com/watch?v=_i4Yxeh5ceQ&t=275s
def climbS(num:int)->int:
    one, two = 1, 1
    for i in range(num - 1):
        temp = one
        one = one + two
        two = temp
    return one

print(climbS(5))