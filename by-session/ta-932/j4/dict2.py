# INPUT:
#ali
#20
#18
#17
#0
#hassan
#19
#20
#0
#.

d = {}
while True:
    name = raw_input()
    if name == '.':
        break
    while True:
        x = float(raw_input())
        if abs(x) < 0.0000001:
            break
        if name not in d:
            d[name] = []
        d[name].append(x)

#d = {'x': [1, 2], 'y': [2, 4]}
for k, v in d.items():
    avg = 0
    for grade in v:
        avg += grade
    avg /= max(1, len(v))
    print k, '=', avg

#l = [1, 2, 3]
#for x in l:
#    print x
#
#i = 0
#while i < len(l):
#    print l[i]


