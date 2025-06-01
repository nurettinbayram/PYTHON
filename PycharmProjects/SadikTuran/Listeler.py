from itertools import count

my_list = [3, 7, 2, 9, 7, 4, 7]

print(len(my_list))
print(my_list.count(7))
print(my_list[0], my_list[-1])

s =set() # baslangic degeri tanimlama
for i in my_list:
    if my_list.count(i) >1:
        s.add(i)
print(s)


even = [i for i in my_list if i%2==0]
odd = [i for i in my_list if i%2==1]
print(even)
print(odd)

s1 = set(my_list)
print(s1)

tekrareden =list({i for i in my_list if my_list.count(i)>1}) # tekrar edenleri tekrarlamamak icin icerde set kullandik
birKereGecen=[i for i in my_list if my_list.count(i)==1]
print(tekrareden)
print(birKereGecen)

print(sum(my_list)/len(my_list))
toplam=0
adet=0
for i in my_list:
    toplam+=i
    adet+=1
print(toplam/adet)

my_list.reverse()
print(my_list)

li = my_list[::-1]
print(li)
my_list.sort()
print(my_list)

my_list = [3, 7, 2, 9, 7, 4, 7]
print("siralanmis", sorted(my_list))
print("orijinal", my_list)

li = sorted(my_list)
li.reverse()
print(li)

print(li[0:3])
print(li[0], li[-1])

print(li[int(len(li)/2)])
my_list = [3, 7, 2, 9, 7, 4, 7, 5]
x=[]
x.append(my_list[int(len(my_list)/2)-1])
x.append(my_list[int(len(my_list)/2)])

print(x)