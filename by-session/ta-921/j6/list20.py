s = "jh32jh32kj"
t = ''

for i in range(len(s)):
    if i % 2 == 0:
        t += s[i]

r = ''
for i in range(len(s)):
    if s[i] not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
        r += s[i]
print r
