

def find(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1


def binary_search(a, x):
    if len(a) == 0:
        return -1
    if len(a) == 1:
        return 0 if x==a[0] else -1

    l = len(a)
    m = l / 2
    M = a[m]
    a1 = a[:m]
    a2 = a[m+1:]

    if M == x:
        return m
    elif x < M:
        return binary_search(a1, x)
    else:
        return m + binary_search(a2, x) + 1


a = [1, 2, 4, 5, 7, 11]
x = 7
print find(a, x)