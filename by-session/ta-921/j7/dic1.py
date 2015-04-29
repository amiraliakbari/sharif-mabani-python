d = {
    'home': 'khane',
    'room': 'otagh',
}

age = {
    'a': 18,
    'b': 17,
    'x': 18,
    'c': 20,
}

print age['x']

for k, v in age.items():
    if v >= 18:
        print k

for k in age.keys():
    print k

for v in age.values():
    print v

a = age.keys()
print a

for k in sorted(age.keys()):
    print k, '=', age[k]
