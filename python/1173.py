n = [i for i in range(10)]

n[0] = int(input())

print('N[{}] = {}'.format(0, n[0]))
for j in range(1, len(n)):
    n[j] = n[j - 1] * 2
    print('N[{}] = {}'.format(j, n[j]))
