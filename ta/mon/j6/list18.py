s = "Salam! abc! jhkfdh"
k = s.find(' ')
j = s.rfind('!')
print s[k+1:j]

def my_find(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1

print my_find([1, 2, 3], 3)
