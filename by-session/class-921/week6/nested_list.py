n_list = [[1, 2], [3, [4,5]], {"ali": ["salam"]}]

for a in n_list:
    print a
print n_list[0][0]
print n_list[2]
print n_list[2]["ali"]
print n_list[2]["ali"][0]
print n_list[2]["ali"][0][0]
print n_list[2]["ali"][0][0][0][0][0][0][0]
print n_list[2].values()

#1 2
#3 4
#5 6
a = [[1, 2], [3, 4], [5, 6]]
print a[2][1]




