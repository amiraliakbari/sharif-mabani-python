
x = 1
y = 1
for i in range(10):
    print x,
    x = x * 2
    print y,
    y = y * 3

for i in range(8):
    if i % 2 == 1:
        print 2**(i/2 + 1),
    else:
        print 3**((i-1)/2),
