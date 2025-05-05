
names = ['Ali', 'Yagmur', 'Hakan', 'Deniz']
years = [1998,2000,1998,1987]

result =""
names.append("Cenk")
names.insert(0, "Sena")
names.remove("Deniz")
result = names.index("Ali")
# result = names.index("Deniz") deniz listede yok
result = names.index("Sena")
result = "Sena" in names
result = "Deniz" in names
result = "Ali" in names
names.reverse()
names.sort()
names.reverse()
years.sort()
s = "Toyota, Honda"
li = s.split(",")
result = max(years)
result = min(years)
result = years.count(1998)
result = years.count(2000)
years.clear()
years =[]
'''
for i in range(3):
    inp = input("yil giriniz : ")
    years.append(inp)
'''


''' nurettin bayram '''
xx = '''--------------------------alt satira kaymak icin kullanilir-------------
devam ediyor---------------------------------------------------
bitti.-----------------------------------------'''

print(xx)

print("names :", names)
print("result :", result)
print("yeras :", years)
print("li :", li)

