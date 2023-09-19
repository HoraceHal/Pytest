x = 1
while x < 10:
    y = 1
    while y <= x:
        print(' %d * %d = %d\t' % (y, x, x * y), end='')
        y += 1
    print('')
    x += 1
