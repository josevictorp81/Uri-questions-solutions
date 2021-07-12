n = [i for i in range(1000)]

t = int(input())
v = 0

for i in range(len(n)):
    n[i] = v
    v += 1
    if v == t:
        v = 0

for i in range(len(n)):
    print('N[{}] = {}'.format(i, n[i]))
