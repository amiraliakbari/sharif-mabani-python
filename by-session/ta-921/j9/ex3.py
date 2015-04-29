#encoding=utf-8
#{
#    'ali': [17, 19, 20],
#    'b': [18, 17],
#}
print u'سلام'
d = {}

while True:
    line1 = raw_input()
    if line1 == 'end':
        break
    a = line1.split(',')
    name = a[0]
    grade = int(a[1])

    if name not in d:
        d[name] = []
    d[name].append(grade)
    print d

#for x in d.keys():
#    print x


for k, v in d.items():
    s = 0
    for x in v:
        s += x
    print k, '=', s/(1.0 * len(v))


