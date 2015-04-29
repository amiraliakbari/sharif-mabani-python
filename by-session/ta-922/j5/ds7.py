d = {
    'x': 2,
    'y': 3,
}

for k, v in d.items():
    print '\t', k, '=', v

print '=============='
l = d.keys()
l.sort()


for i in range(len(l)):
    print '\t', l[i], '=', d[l[i]]