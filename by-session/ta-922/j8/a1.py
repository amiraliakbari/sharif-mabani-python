key = {
    ' ': ' ',
    '4': 'A',
    '8': 'B',
    '(': 'C',
}


print key['4']

filename = raw_input()
f = open(filename, 'r')
s = f.read()

p = s.split(',')
p = p[1:-1]
a = []

for x in p:
    if ';' in x or (' ' not in x and x in key.keys()):
        b = x.split(';')
        a = a + b
        a.append(' ')

t = ''
for ch in a:
    t += key[ch]
t += '.'
print t
