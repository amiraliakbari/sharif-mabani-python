def dis(x1, y1, x2, y2):
    dx = (x1 - x2) ** 2
    dy = (y1 - y2) ** 2
    return (dx + dy) ** 0.5

ax = 10
ay = 6

bx = 5
by = 9

ox = 4
oy = 4

d1 = dis(ax, ay, ox, oy)  # dis A -- O
d2 = dis(bx, by, ox, oy)  # dis B -- O

if d1 < d2:
    print 'AO < BO'
else:
    print 'AO >= BO'
