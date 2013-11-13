n = 10
x = 1
i = 1
while x < 200:
    print x,
    x = x + i
    i = i + 1
    if x < 200:
        print ',',
