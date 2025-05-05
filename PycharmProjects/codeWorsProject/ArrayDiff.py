# Implement a function that computes the difference between two lists. The function should
# remove all occurrences of elements from the first list (a) that are present in the second
# list (b). The order of elements in the first list should be preserved in the result.

def array_diff(a,b):
    c=[]
    for i in a:
        if i in b:
            continue
        else:
            c.append(i)
    return c

a = [1, 2, 2, 2, 3]
b = [2]

print(array_diff(a,b))

# II.yol
# def array_diff(a, b):
#     return [x for x in a if x not in b]