n = int(input())

field, mincost, prev, vis = [[0 for j in range(n + 1)] for i in range(n + 1)], [[0 for j in range(n + 1)] for i in range(n + 1)], [[0 for j in range(n + 1)] for i in range(n + 1)], [[0 for j in range(n + 1)] for i in range(n + 1)]

for i in range(1, n + 1):
    k = 1
    for j in input().split():
        field[i][k] = int(j)
        k += 1

for i in range(n + 1):
    mincost[i][0] = 1000000000000000000000
    mincost[0][i] = 1000000000000000000000

mincost[0][1] = 0
mincost[1][0] = 0

for i in range(1, n + 1):
    for j in range(1, n + 1):
        mincost[i][j] = field[i][j] + min(mincost[i - 1][j], mincost[i][j - 1])
        if (mincost[i - 1][j] == mincost[i][j - 1]) or (mincost[i - 1][j] < mincost[i][j - 1]):
            prev[i][j] = 'U'
        else:
            prev[i][j] = 'L'

for i in range(1, n + 1):
    for j in range(1, n + 1):
        vis[i][j] = '.'

vis[n][n] = '#'
k, m = n, n
while (k >= 1) and (m >= 1):
    if prev[k][m] == 'U':
        vis[k - 1][m] = '#'
        k -= 1
    else:
        vis[k][m - 1] = '#'
        m -= 1

for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(vis[i][j], end = ' ')
    print()
