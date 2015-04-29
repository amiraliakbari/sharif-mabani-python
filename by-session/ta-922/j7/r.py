def f(n):
    if n == 0:
        return []
    if n == 1:
        return ['0', '1']
    if n == 2:
        return ['00', '01', '10', '11']
    r = []
    s = f(n-1)
    for x in s:
        x1 = '0' + x
        r.append(x1)
        x2 = '1' + x
        r.append(x2)
    return r
