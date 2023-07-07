m, n, mins = map(int, input().split())

arr = [[0 for i in range(n + 2)] for j in range(m + 2)]

for i in range(mins):
    x, y = map(int, input().split())
    arr[x][y] = -400000000
    arr[x - 1][y] += 1
    arr[x][y - 1] += 1
    arr[x + 1][y] += 1
    arr[x][y + 1] += 1
    arr[x - 1][y - 1] += 1
    arr[x + 1][y + 1] += 1
    arr[x - 1][y + 1] += 1
    arr[x + 1][y - 1] += 1

for i in range(1, m + 1):
    for j in range(1, n + 1):
        if (arr[i][j] < 0):
            print('*', end='')
        elif (arr[i][j] == 0):
            print('.', end='')
        else:
            print(arr[i][j], end='')
    print()