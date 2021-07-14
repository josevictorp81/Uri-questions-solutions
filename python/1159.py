while True:
    x = int(input())
    
    soma = 0
    if x == 0:
        break
    
    if x % 2 == 0:
        for i in range(x, x + 9, 2):
            soma += i
        print(soma)
    else:
        for i in range(x + 1, x + 10, 2):
            soma += i
        print(soma)
    