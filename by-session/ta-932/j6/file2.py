# a.txt:
#10 20 50 60
#20 10
#90 20

# 50
# 15
# 55


for l in open('a.txt'):
    l = l.strip()
    a = l.split(' ')
    s = 0
    for x in a:
        s += x
    s /= max(len(a), 1)
    print s
