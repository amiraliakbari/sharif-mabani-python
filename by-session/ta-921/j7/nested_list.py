a = ['aaa', 'bb', 'cc']
b = [1, 2, 'ccc', 4, 2.4]

x = b[2]
y = b[-1]

c = [[1, 2, 4], [2, 3], [5]]
t = c[0]
#print t[1]

#print c[1][1]


for x in c:
    for y in x:
        print y,
    print ''

