def selection_sort(lis):
    for i in range(len(lis)):
        for j in range(i, len(lis)):
            if lis[i] > lis[j]:
                temp = lis[i]
                lis[i] = lis[j]
                lis[j] = temp

def buble_sort(lis):
    for i in range(len(lis)):
        print lis
        for j in range(len(lis) - 1):
            if lis[j] > lis[j + 1]:
                te = lis[j]
                lis[j] = lis[j + 1]
                lis[j + 1] = te

def insertion_sort(lis):
    for i in range(1, len(lis)):
        print lis
        j = i
        while (j > 0) and (lis[j] < lis[j - 1]):
            te = lis[j]
            lis[j] = lis[j - 1]
            lis[j - 1] = te
            j = j - 1

l = [9,6,4,3,7,5,1,2,8,]
#l = [9,8,7,6,5,4,3,2,1,]
insertion_sort(l)
print l
