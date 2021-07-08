i = 0
j = 1
while i <= 2:
    for k in range(3):
        if i == 0 or i == 1.0 or i > 1.8:
            print('I={:.0f} J={:.0f}'.format(i,j))
        else:
            print('I={:.1f} J={:.1f}'.format(i,j))
        j += 1
    i += 0.2
    j = 1 + i