n = []
ni = []

for i in range(20):
    n.append(int(input()))
    ni.insert(0, n[i])

for i in range(20):
    print('N[{}] = {}'.format(i, ni[i]))
