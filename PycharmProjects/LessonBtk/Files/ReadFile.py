import json

my_file = open("test.txt", "r", encoding="utf-8") #okuma islemi
result = my_file.read() # tum dosya okunur resulta atanir.

print("Bastan okuma ---> " + result)
print("imlege sona alinmis Okuyabilir mi? ---> " + my_file.read()) # imle en sonda oldugu icin herhangi bir islem yapilmiyor.

my_file.seek(0) # imlegi basa alma
print("imlegi basa aldiktan sonra okunuyor mu? ---> " + my_file.read())

my_file.seek(0)
print("readline ne ise yarar? --> " + my_file.readline())
print(my_file.readline()) # satir satir okuma islemi gerceklestirir

# config.json okuma
with open("config.json", "r") as f:
    info = json.load(f)
    print(info["username"])
    print(info["password"])

