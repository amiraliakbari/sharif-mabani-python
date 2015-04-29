d = {}


def avg(l):
    s = 0
    for i in range(len(l)):
        s += l[i]
    return float(s) / len(l)


n = int(raw_input())
for i in range(n):
    line = raw_input()
    a = line.split(',')
    stdid = a[0]
    grade = a[2]

    if not stdid in d:
        d[stdid] = []
    if d.keys().find(stdid) == -1:
        d[stdid] = []
    d[stdid].append(grade)


for k, v in d.items():
    print k, '=', avg(v)

