my_file = open("test.txt", "w", encoding="utf-8") # imleci basatan alip yazdirir
print(my_file)
my_file.write("nurettin bayram\t") # write()  metodu her cagrildiginda kaldigi yerden devam eder
my_file.write("dosya yonetimi\n")
my_file.write("yeni satir")

my_file = open("test.txt", "w", encoding="utf-8") # yeniden dosya acma islemine girildiginden imlec tekrar bastan alinir
my_file.write("silinip yeniden yazildi.\n") # ilendeki yarakter sayidsi kadar digerinin uzerine yazdirilir.
my_file.write("alt satirdan devam edilir")

print(my_file.writable() , " -> dosya yazilabilir mi?")



my_file.close()