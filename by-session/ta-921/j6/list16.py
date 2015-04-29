s = "Salam abc"

if ' ' in s:
    print 'Fasele darad'

print s.find(' ')
print s.find('x')

c = 's'
if s.find(c) > -1:
    print 'hast'

q = 'salAM'
print s.find(q)

s1 = s.lower()
q1 = q.lower()
print s1.find(q1)

print s.lower().find(q.lower())

