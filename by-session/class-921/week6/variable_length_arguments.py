def aa():
    return 1, 2

a, b = aa()

print a
print b

def sum(param1, *argumans):
    s = 0
    print param1
    print argumans
    for i in argumans:
        s = s + i
    return s

print sum(1, 2, 3, 4, 5, 6, 7, 8)

def aaa(**argumans):
    print argumans

aaa(a = 1, b = 2, c = 3, d = 4)







