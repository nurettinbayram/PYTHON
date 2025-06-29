nums = [5,20,66,1314]

arr = [abs(x) for x in nums]
maxim = max(arr)

digits = [int(digit) for digit in str(maxim)]

print(max(digits))



############################

num = 25348
digits = [int(digit) for digit in str(num)] #elimizdeki sayiyi for ile strye cevirir sonra her karakteri digite atar
# ve digiti int yapip dizi dondurur
print(digits)