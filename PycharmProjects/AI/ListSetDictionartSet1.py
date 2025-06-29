# Bir listede yalnızca tekil (bir kez geçen) elemanları döndüren bir Python fonksiyonu yaz.

my_list = [1, 2, 2, 3, 4, 4, 5, 6, 7, 8, 9, 9,10]

def oddList(li):
    odd=[]
    for i in li:
        if i%2 ==1:
            odd.append(i)
    return odd

print(oddList(my_list))

def uniqueElements(li):
    result=[]
    for i in li:
        if li.count(i)==1:
            result.append(i)
    return result
print(uniqueElements(my_list))

# İlk 3 elemanı içeren yeni bir tuple,
# Son 3 elemanı içeren başka bir tuple oluştur ve ekrana yazdır.

my_tuple = (10, 20, 30, 40, 50, 60)

first3 = my_tuple[:3]
last3 = my_tuple[-3:]

print("First 3:", first3)
print("Last 3:", last3)



# Bu sözlükte notu 80'den büyük olan öğrencileri ve notlarını içeren yeni bir sözlük oluştur.

students = {
    "Ali": 85,
    "Ayse": 92,
    "Mehmet": 78,
    "Zeynep": 95,
    "Ahmet": 60
}

# I. YOL
high_scores = {k: v for k, v in students.items() if v > 80}
print(high_scores)

# II. YOL
newStu1={}
for k, v in students.items():
    if v > 80:
        newStu1.setdefault(k,v)
print(newStu1)

# III. YOL
newStu={}
for k, v in students.items():
    if v > 80:
        newStu.update({k:v})
print(newStu)


# Aşağıdaki iki listeden ortak elemanları içeren bir set oluştur:
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

# I YOL
newList =[i for i in list1 if i in list2]
print(newList)
# II YOL
unCommonSet = set(list1) ^ set(list2)
print(unCommonSet)
# II YOL
commonSet = set(list1) & set(list2)
print(commonSet)
# III YOL
newSet ={i for i in list1 if i in list2}
print(newSet)

# iki set arasindaki modifation
a = {1, 2, 3}
b = {3, 4, 5}

print(a.union(b))              # {1, 2, 3, 4, 5}
print(a.intersection(b))       # {3}
print(a.difference(b))         # {1, 2}
print(a.symmetric_difference(b))  # {1, 2, 4, 5}