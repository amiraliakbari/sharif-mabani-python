import random

#from random import *
#random()
#choice()

random.seed()
print '\t', random.randrange(0, 10)
print '\t', random.random()
print '\t', random.choice([1, 6, 90])


def randrange(a, b):
    r = random.random()
    return a + (b - a + 1) * r

def choice(l):
    ind = random.randrange(0, len(l))
    return l[ind]
