def order(sentence):
    if not sentence:
        return ""

    words = sentence.split()
    sorted_words = sorted(words, key=lambda word: int(''.join(filter(str.isdigit, word))))

    return " ".join(sorted_words)

print(order("is2 Thi1s T4est 3a"))

    # 📌 Genel Algoritma Akışı
    # Örneğin, ["is2", "Thi1s", "T4est", "3a"] listesi için sıralama nasıl çalışır?
    #
    # "is2" için:
    #
    # filter(str.isdigit, "is2") → ['2']
    #
    # ''.join(['2']) → "2"
    #
    # int("2") → 2
    #
    # "Thi1s" için:
    #
    # filter(str.isdigit, "Thi1s") → ['1']
    #
    # ''.join(['1']) → "1"
    #
    # int("1") → 1
    #
    # "T4est" için:
    #
    # filter(str.isdigit, "T4est") → ['4']
    #
    # ''.join(['4']) → "4"
    #
    # int("4") → 4
    #
    # "3a" için:
    #
    # filter(str.isdigit, "3a") → ['3']
    #
    # ''.join(['3']) → "3"
    #
    # int("3") → 3
    #
    # Şimdi sorted() bu değerlere göre sıralama yapar:

#Thi1s (1) → is2 (2) → 3a (3) → T4est (4)
