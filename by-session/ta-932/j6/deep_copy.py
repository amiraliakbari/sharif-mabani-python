def copy(a):
    b = []
    for x in a:
        b.append(x)
    return b


def deep_copy(a):
    if isinstance(a, int) or isinstance(a, float):
        return a

    b = []
    for x in a:
        b.append(deep_copy(x))
    return b