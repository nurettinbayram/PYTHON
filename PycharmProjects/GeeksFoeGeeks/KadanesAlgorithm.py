##Given an integer array arr[]. You need to find the maximum sum of a subarray.

def max_subarray_sum(arr):
    max_so_far = arr[0]
    curr_max = arr[0]

    for i in range(1, len(arr)):
        # Ya mevcut elemanı alırız, ya da mevcut toplamın üzerine ekleriz
        curr_max = max(arr[i], curr_max + arr[i])
        print(curr_max)
        max_so_far = max(max_so_far, curr_max)
        print(max_so_far)
        print("-------------------")

    return max_so_far

# Örnek kullanım
arr = [2, 3, -8, 7, -1, 2, 3]
print(max_subarray_sum(arr))  # Output: 11

