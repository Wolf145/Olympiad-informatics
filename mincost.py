n = int(input())
arr = [[0 for i in range(n)] for j in range(n)]
mincost = [0 for i in range(n + 1)]

for i in range(n):
    o = input().split()
    for j in range(len(o)):
        arr[i][i + j] = int(o[j])

for i in range(1, n + 1):
    mincost[i] = 100000000000000000
    for j in range(i):
        if mincost[j] + arr[j][i - 1] < mincost[i]:
            mincost[i] = mincost[j] + arr[j][i - 1]

print(mincost[n])
