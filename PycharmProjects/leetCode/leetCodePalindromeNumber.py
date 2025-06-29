x = 123
num = [n for n in str(x)]

y = [num[j] for j in range(len(num)-1, -1, -1)]
print(num)
print(y)
print(y == num)


############### baska bir yol ####################
if x < 0:
    print(False)

x_str = str(x)
print( x_str == x_str[::-1])