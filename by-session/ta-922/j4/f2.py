
def square(x):
    return x * x

print square(3)

a = square(5)
print a + 1

if square(a) < 100:
    print 'X'


def print_salam(name):
    print 'Salam ' + name

print_salam('ali')



def sum(l):
    s = 0
    for i in range(len(l)):
        s += l[i]
    return s

def count(l):
    s = 0
    for i in range(len(l)):
        s += 1
    return s

def min(a, b):
    if a < b:
        return a
    return b

def min_list(l):
    m = l[0]
    for i in range(len(l)):
        if l[i] < m:
            m = l[i]
    return m


def devisors(n):
    s = 0
    for i in range(len(n)):
        if n % i == 0:
            s += 1
    return s


def is_prime(n):
    d = devisors(n)
    if d == 2:
        return True
    return False
