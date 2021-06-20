while True:
    m, n = list(map(int, input().split()))
    
    if m <= 0 or n <= 0:
        break
    if m > n:
        m, n = n, m
    
    soma = 0
    for i in range(m, n + 1):
        soma += i
        print('{}'.format(i), end=' ')
    print('Sum={}'.format(soma))