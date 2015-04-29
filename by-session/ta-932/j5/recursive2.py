

a = [1, 2, 6, 7, 9, 10, 20, 30]


def search_linear(a, x):
    for y in a:
        if x == y:
            return True
    return False

def search_linear_index(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1

def search_binary(a, x):
    n = len(a)
    if n == 0:
        return False
    if n == 1:
        return a[0] == x


    mid = n / 2

    m = 0
    left = []
    right = []
    for i  in range(n):
        if i < mid:
            left.append(a[i])
        elif i == mid:
            m = a[i]
        else:
            right.append(a[i])

    m = a[mid]
    left = a[:mid]
    right = a[mid+1:]

    if m == x:
        return True
    elif m < x:
        return search_binary(right, x)
    else:
        return search_binary(left, x)

    if m == x:
        return mid
    elif m < x:
        return mid + search_binary(right, x)
    else:
        return search_binary(left, x)






