v = [x for x in range(10)]

for i in range(len(v)):
    v[i] = int(input())

for i in range(len(v)):
    if v[i] <= 0:
        v[i] = 1
    print('X[{}] = {}'.format(i, v[i]))