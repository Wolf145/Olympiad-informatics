n = int(input())
a = [[0, 0, 0] for i in range(n + 2)]
sum1 = 0

for i in range(n):
    a[i] = [int(i) for i in input().split()]

for i in range(0, n, 3):
    if n > 3:
        if (0 not in a[i + 1]) and (0 not in a[i + 2]):
            sum1 += min(a[i][0] + a[i + 1][0] + a[i + 2][0], a[i][2], a[i][1] + a[i + 2][0], a[i][0] + a[i + 1][1])
    else:
        sum1 += min(a[i][0] + a[i + 1][0] + a[i + 2][0], a[i][2], a[i][1] + a[i + 2][0], a[i][0] + a[i + 1][1])

print(sum1)
