a = [1, 6, 7, 9, 11, 14]
x = 11

if x in a:
    print 'hast'

def bs(a, x):
    if len(a) == 0:
        return False
    if len(a) == 1:
        if a[0] == x:
            return True
        return False

    n = len(a)
    m = a[n/2]
    a1 = a[:n/2]
    a2 = a[n/2+1:]

    if m == x:
        return True
    if x < m:
        hast = bs(a1, x)
        return hast
    if x > m:
        return bs(a2, x)
