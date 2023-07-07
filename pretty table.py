ans = ''
for k in range(int(input())):
    n, m = map(int, input().split())
    ar = [[int(i) for i in input().split()] for j in range(n)]
    if (n == 1 or m == 1):
        ans += 'YES\n'
    else:
        f = 0
        for l in range(n - 1):
            for t in range(m - 1):
                s = ar[l][t] + ar[l + 1][t] + ar[l][t + 1] + ar[l + 1][t + 1]
                if (s == 4 or s == 0):
                    f = 1
        if (f):
            ans += 'NO\n'
        else:
            ans += 'YES\n'
print(ans)
