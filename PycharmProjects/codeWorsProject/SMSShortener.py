# SMS messages are limited to 160 characters. It tends to be irritating, especially when freshly written message is 164
# characters long.
# Your task is to shorten the message to 160 characters, starting from end, by replacing spaces with camelCase, as much as necessary.
# If all the spaces are replaced but the resulting message is still longer than 160 characters, just return that resulting message.

def shorten_sms(message):
    if len(message) <= 160:
        return message

    words = message.split()
    if len(words) == 1:
        return message  # tek kelimeyse boşluk yok, hiçbir şey yapamayız

    # Baştan kelimeleri al, camelCase'e çevirmeye sondan başlayacağız
    new_words = [words[0]]
    for word in words[1:]:
        new_words.append(' ' + word) ##burada yeni disi olusturmasinin sebebi elemanlari bosluklar ile dizide turmak

    # Tersten gidip boşlukları camelCase'e çevirelim
    for i in range(len(new_words) - 1, 0, -1):
        if len(''.join(new_words)) <= 160:
            break
        # boşluğu camelCase'e çevir
        new_words[i] = new_words[i][1].upper() + new_words[i][2:] # ' hello' --> 'Hello'  ##bosluga dikkat

    result = ''.join(new_words)
    return result

str = ("No one expects the Spanish Inquisition! Our chief weapon is surprise, fear and surprise; "
       "two chief weapons, fear, surprise, and ruthless efficiency! And that will be it.")
print(shorten_sms(str))



