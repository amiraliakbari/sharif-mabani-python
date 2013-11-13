import math
def sin(rad, precision):
    '''
    rad is angle  in radians
    precision is a floating point number which defines the maximum precision
    returns the value of sin(rad)
    '''
    rad = rad % math.pi
    i = 1
    res = rad
    tmp = rad
    while 1:
        tmp = tmp * (-1.0) * rad * rad /  (4 * i * i + 2*i)
        res = res + tmp
        if abs(tmp) <= abs(precision):
            return res

# print sin(math.pi/6,0.001)
print sin(precision=.000000000000000000001,rad=math.pi/12.0)
print math.sin(math.pi/12.0)