def distance(x1, y1, x2, y2):
    dx = (x1 - x2)**2
    dy = (y1 - y2)**2
    d = (dx + dy)**0.5
    return d

ax = 10
ay = 6

bx = 5
by = 9

ox = 4
oy = 4

if distance(ax, ay, ox, oy) < distance(bx, by, ox, oy):
    print "Point B"
else:
    print"Point A"
