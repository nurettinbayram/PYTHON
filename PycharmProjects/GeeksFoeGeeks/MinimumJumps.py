##You are given an array arr[] of non-negative numbers. Each number tells you the maximum number of steps
# you can jump forward from that position.
# Input: arr[] = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
# Output: 3
# Explanation: First jump from 1st element to 2nd element with value 3. From here we jump to 5th element with value 9,
# and from here we will jump to the last.
def min_jumps(arr):
    n = len(arr)
    if n <= 1:
        return 0  # Zaten son noktadayız
    if arr[0] == 0:
        return -1  # İlk adımda bile ilerleyemiyoruz

    # maxReach: şu ana kadar ulaşabileceğimiz en uzak yer
    # steps: bu aralıktaki kalan adım sayısı
    # jumps: toplam sıçrama sayısı
    maxReach = arr[0]
    steps = arr[0]
    jumps = 1

    for i in range(1, n):
        # Sona ulaşıldıysa
        if i == n - 1:
            return jumps

        # maxReach’i güncelle
        maxReach = max(maxReach, i + arr[i])

        # Bir adım attık
        steps -= 1

        # Adım kalmadıysa
        if steps == 0:
            jumps += 1

            # Yeni adımların olup olmadığına bak
            if i >= maxReach:
                return -1  # Daha ileri gidemeyiz

            # Yeni aralık için adım sayısını güncelle
            steps = maxReach - i

    return -1  # Son noktaya ulaşamıyorsak

arr = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
print(min_jumps(arr))