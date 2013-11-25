def my_print(s, *args):
    #print s, args
    for i in range(len(args)):
        s = s.replace('{' + str(i) +'}', args[i])
    print s
    #s = s.replace('{1}', p1)
    #s = s.replace('{2}', p2)
    #print s

my_print('Salam!')
my_print('Salam {0}!', 'ali')
my_print('Salam {0}! {1}', 'ali', 'X')
