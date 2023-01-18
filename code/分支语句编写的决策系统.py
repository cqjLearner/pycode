a = input('1:')
b = input('2:')
c = input('3:')
d = int(input('score:'))
if (a=='通过') and (b=='通过'):
    e=1
else:
    if (a=='通过') or (b=='通过'):
        if ((a=='通过') and (c=='通过')) or ((b=='通过') and (c=='通过')):
            e=1
        else:
             e=0
    else:
        e=0
if (d>=60) and e:
    print('pass')
else:
    print('not pass')
