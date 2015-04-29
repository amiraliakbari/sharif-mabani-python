x = 1
y = 1

print x,
print y,
for i in range(10):
    z = x + y
    print z,
    x = x + y
    x = y
    y = z
