def binary_search(min, max):
    mid = (min + max) / 2
    s = raw_input("aya adad = %d" % mid)
    if (s == "="):
        print "hoooora!"
    elif s == "<":
        binary_search(min, mid)
    elif s == ">":
        binary_search(mid + 1, max)

binary_search(1, 2)#number = 2