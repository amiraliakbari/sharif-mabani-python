import math

x = int(raw_input())
print math.sin(x)

from math import sin

print sin(x)


from x.y.b import f1
#import b




print x + b.f1() + b.g()


















a = [1, 2, 3, 1, 2, 6, 3]

b = []
for x in a:
    if x not in b:
        b.append(x)


s = 'aaaaabbbbbbhhhhhhdkkkxxxxaaaaaa'
t = ''
for ch in s:
    if len(t) > 0 and t[-1] != ch:
        t += ch
print t
# >> 'abhdkxa'


s = set()
s.add(1)
s = set(a)
print s
{1, 2, 3, 6}
