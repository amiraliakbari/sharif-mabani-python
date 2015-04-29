x = 0

def rand(n):
    global x
    x = x * x + 6 * x + 9
    return x % n


#print '\t', rand(7)
#print '\t', rand(7)
#print '\t', rand(7)


import random

print random.random()
print '\t', random.choice(range(10))
