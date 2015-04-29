n = int(raw_input())

i = 0
while i < n:
    S = ''
    while True:
        s = raw_input()
        if s == '#':
            break
        if s == '1':
            S += 'a'
        S += s
    print S
    i += 1

x = 2
x = '2'