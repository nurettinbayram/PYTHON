myList = []
for _ in range(int(input())):
    name = input()
    score = float(input())
    myList.append([name, score])

myList.sort()
print("myList : " , myList)
dic = dict(myList)
print("dic : ", dic)
dic2 = list(set(dic.values()))
dic2.sort()
print("dic2 : ",  dic2)
li =[]
val = dic2[1]
for i, j in dic.items():
    if j == val:
        print(i)