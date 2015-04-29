def drange(start, stop, step):
    '''
    produces numbers with given step in the given range
    '''
    r = start
    while r < stop:
        yield r
        r += step

def simpleIntegration(lower,upper,a,b,c, delta):
    '''
    integration of second degree polynomial:
    a * x**2 + b*x + c
    using simple rectangle method
    '''
    res = 0
    for x in  drange(lower,upper,delta):
        res = res + (a * x**2 + b * x + c) * delta
    return res

print simpleIntegration(0,1,3,2,1,0.0001)

