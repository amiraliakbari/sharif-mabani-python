d = {
    '92100': 20,
    '92200': 18,
    '80100': 17,
}


print d['80100']


d2 = {
    'cat': 'gorbe',
    'dog': 'sag',
}

x = d2['cat']

#d2['cat'] = 'XXXX'
d2['book'] = 'ketab'


#word = raw_input()
#print d2[word]

word = raw_input()
mani = raw_input()
d2[word] = mani


line= raw_input()
a = line.split(',')
word = a[0]
mani = a[1]
d2[word] = mani
