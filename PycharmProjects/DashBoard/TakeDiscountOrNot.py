"""
İlk satır: T → test durumu sayısı
Her test için:
Satır 1: N X Y
N → ürün sayısı
X → kuponun fiyatı
Y → ürünlerden düşülecek indirim miktarı
Satır 2: A1 A2 ... AN → ürünlerin fiyatları listesi

Ürünler: [20, 15, 10]
Kuponsuz toplam: 20+15+10 = 45
Kuponla:
İndirimli ürünler: [15, 10, 5]
Toplam: 15+10+5 = 30
Artı kupon fiyatı (10) → toplam = 40
Kar: 45 > 40 → Chef kupon alır → COUPON
"""
# https://www.codechef.com/practice/course/arrays/ARRAYS/problems/DISCOUNTT

t = int(input())

while t > 0:
    n, x, y = map(int, input().split())
    prices = list(map(int, input().split()))
    save = 0

    for price in prices:
        if price >= y:
            save += y
        else:
            save += price

    if save > x:
        print("COUPON")
    else:
        print("NO COUPON")
    t -= 1