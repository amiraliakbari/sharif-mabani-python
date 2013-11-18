def merge_sort(lis):
    if len(lis) < 2:
        return
    lis1 = []
    lis2 = []
    for i in range(len(lis) / 2):
        lis1.append(lis[i])
    for i in range(len(lis) / 2, len(lis)):
        lis2.append(lis[i])
    merge_sort(lis1)
    merge_sort(lis2)
    i = 0
    j = 0
    while (len(lis) > 0):
        del lis[0]
    while (i < len(lis1)) and (j < len(lis2)):
        if lis1[i] < lis2[j]:
            lis.append(lis1[i])
            i = i + 1
        elif lis1[i] > lis2[j]:
            lis.append(lis2[j])
            j = j + 1
    while (i < len(lis1)):
        lis.append(lis1[i])
        i = i + 1
    while (j < len(lis2)):
        lis.append(lis2[j])
        j = j + 1


l = [9,6,4,3,7,5,1,2,8,]
merge_sort(l)
print l
