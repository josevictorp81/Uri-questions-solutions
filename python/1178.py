n = [i for i in range(100)]
x = float(input())

n[0] = x
print('N[{}] = {:.4f}'.format(0, n[0]))
for i in range(1, len(n)):
    x /= 2
    n[i] = x
    
    print('N[{}] = {:.4f}'.format(i, n[i]))
