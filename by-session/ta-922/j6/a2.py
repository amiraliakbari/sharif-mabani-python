

s = open('a.txt', 'r').read()
a = s.split('\n')


c = 0
for l in open('a.txt'):
    l = l.strip()
    a = l.split(',.!? \n\t')
    c2 = 0
    for x in a:
        if x != '':
            c2 += 1
    c += c2

    #for i in range(len(a)):
    #    x = a[i]
    #    ...

s = 'gdshbdxcgxjhcxkj'
t = ''
for i in range(len(s)):
    if s[i] != 'x':
        t += s[i]

t = ''
for ch in s:
    if ch != 'x':
        t += ch