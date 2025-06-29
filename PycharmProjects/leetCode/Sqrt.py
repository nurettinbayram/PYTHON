# def my_sqrt(x):
#     if x<0:
#         print("x sifirdan kucuk olamaz...")
#         return
#     i = 0
#     while i * i <= x:
#         i += 1
#     return i - 1
#
#
# print(my_sqrt(9))


# II. way
def mySqrt(x):
    if x < 2:
        return x

    left, right = 0, x // 2 + 1
    while left <= right:
        mid = (left + right) // 2
        square = mid * mid

        if square == x:
            return mid
        elif square < x:
            left = mid + 1
        else:
            right = mid - 1
    return right


mySqrt(12)