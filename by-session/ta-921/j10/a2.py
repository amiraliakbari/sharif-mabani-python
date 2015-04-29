hc1 = [5, [1, 2, 0]]

def get_name(hc):
    return '2metil heptan'

def get_chain_name(n):
    l = ['', 'metan', 'etan', 'propan']
    return l[n]

def is_isomer(hc1, hc2):
    return get_name(hc1) == get_name(hc2)



n = 8
H = []

for i in range(n, 1, -1):
    hc = [i, [0] * (i-2)]
    found = False
    for h in H:
        if is_isomer(h, hc):
            found = True
            break
    if not found:
        H.append(hc)

for hc in H:
    print get_name(hc)
