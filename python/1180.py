n = int(input())

x = [i for i in range(n)]

x = list(map(int, input().split()))

pos = 0
menor = x[0]
for i in range(len(x)):
    if x[i] < menor:
        pos = i
        menor = x[i]

print('Menor valor: {}'.format(menor))
print('Posicao: {}'.format(pos))
