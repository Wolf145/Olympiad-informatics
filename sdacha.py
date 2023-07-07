k = int(input())
a = [int(i) for i in input().split()]
n = int(input())
f = [0 for i in range(n + 1)]

for m in range(1, n + 1):
    f[m] = 10000000000000
    
    for i in range(k):
        if (m >= a[i]) and (f[m - a[i]] + 1 < f[m]):
            f[m] = f[m - a[i]] + 1

if f[n] == 10000000000000:
    print(-1)
    print('Требуемую сумму выдать невозможно')

else:
    print(f[n])

    while n > 0:
        for i in range(k):
            if f[n - a[i]] == f[n] - 1:
                print(a[i], end=' ')
                n -= a[i]
                break
