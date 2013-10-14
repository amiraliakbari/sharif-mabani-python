def a():
    print k
    global k
    k = 1
    print k

k = 10
a()
print k