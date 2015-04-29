def b():
    print("hooora!")
dic1 = {1: 2, 1: 4}
for i in dic1.items():
    if 'a' == i:
        b()
else:
    break
print ":("