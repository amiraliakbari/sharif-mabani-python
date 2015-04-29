def f(n):
    if n == 0:
        return [[]]
    if n == 1:
        return [[], [1]]
    if n == 2:
        return [[], [1], [2], [1, 2]]

    a = []
    sub_n_1 = f(n-1)
    for x in sub_n_1:
        a.append(x)
    for x in sub_n_1:
        x.append(n)
        a.append(x)
    return a
