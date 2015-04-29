d = {
    'book': ['bouk', 'boook', 'boock'],
    'apple': ['aple', 'appl'],
}

t = 'I and my brother, have a boook about appl.'

t = t.replace(',', ' ')
t = t.replace('.', ' ')
t = t.replace('?', ' ')
t = t.replace('!', ' ')

words = t.split(' ')

t2 = ''
for w in words:
    # w in d
    # w in d.keys()

    if w == '':
        continue

    correct_word = w
    for k, v in d.items():
        if w in v:
            correct_word = k

    t2 += correct_word + ' '


    # a = [1, 23, 8, -1, 5]
    # minimum = a[0]
    # for x in a:
    #     if x < minimum:
    #        minimum = x