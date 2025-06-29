with open("test.txt", "r+", encoding="utf-8") as my_file: # hem okuma hem yazma modunda otomatic kapatma isleminde
    print(my_file.read())


li = ["liste elemanlari\n", "satir satir\n", "eklenebilir\n"]

with open("test.txt", "w", encoding="utf-8") as my_file:
    my_file.writelines(li)