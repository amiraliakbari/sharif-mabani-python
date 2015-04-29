f = open('a.txt', 'w')

f.write('salam\n')
f.write('2\n')

a = 2
b = 'ali'
f.write('salam ' + b + '\n')
f.write('salam %s! %d\n' % (b, a))

print 'salam %s! %d\n' % (b, a)
s = 'salam %s! %d\n' % (b, a)

f.close()

for l in open('a.txt'):
    print l


f = open('a.txt', 'a')
f.write('3')
f.close()


