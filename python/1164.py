n = int(input())

for i in range(n):
    x = int(input())
    
    num = int(x / 2)
    soma = 0
    for j in range(1, num + 1):
        if x % j == 0:
            soma += j
    
    if soma == x:
        print('{} eh perfeito'.format(x))
    else:
        print('{} nao eh perfeito'.format(x))
