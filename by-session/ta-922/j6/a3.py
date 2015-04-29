#a = [1, 2, 5, 6, 6]
#b = [2, 4, 6, 10]

def merge(a, b):
    #c = a + b
    #c.sort()
    #return c

    i = 0
    j = 0
    c = []
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1
    while i < len(a):
        c.append(a[i])
    while j < len(b):
        c.append(b[j])

    return c