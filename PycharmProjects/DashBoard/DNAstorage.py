# https://www.codechef.com/problems/DNASTORAGE

t = int(input("tur sayisini gir: "))
arr=[]

while t>0:
    n = int(input("karakter sayisini gir: "))
    s = input("karakterlerini  gir: ")
    for i in range(0,n,2):
        item =s[i:i+2]
        arr.append(item)
    print(arr)
    dna = ""
    for i in arr:
        match i:
            case "00":
                dna += 'A'
                continue
            case "01":
                dna += 'T'
                continue
            case "10":
                dna += 'C'
                continue
            case "11":
                dna += 'G'
                continue
            case _:
                print("gecersiz karakter.")
    print(dna)
    arr=[]

    t-=1

