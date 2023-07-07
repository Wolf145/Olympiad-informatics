n, k = (int(i) for i in input().split())

ar, ar1 = [int(i) for i in input().split()], [int(i) for i in input().split()]

for i in range(k):
    l, r = 0, n - 1
    while r > l:
        avg = l + (r - l) // 2
        if ar[avg] < ar1[i]:
            l = avg + 1
        else:
            r = avg
    if ar[r] == ar1[i]:
        print('YES')
    else:
        print('NO')
