m, n = (int(i) for i in input().split())
arr = [[0 for i in range(n + 1)] for j in range(m + 2)]
arr1 = [[0 for i in range(n + 1)] for j in range(m + 2)]
prev = [[0 for i in range(n + 1)] for j in range(m + 2)]
path = [0 for i in range(n)]

for i in range(1, m + 1):
    o = input().split()
    for j in range(1, n + 1):
        arr[i][j] = int(o[j - 1])

for i in range(n):
    arr1[0][i] = 1000000000000
    arr1[n][i] = 1000000000000

for i in range(m + 2):
    arr1[i][0] = 0

for j in range(1, n + 1):
    for i in range(1, m + 1):
        arr1[i][j] += min(arr1[i - 1][j - 1], arr1[i + 1][j - 1], arr1[i][j - 1]) + arr[i][j]
        arr[i][j] = arr1[i][j]
        if arr1[i + 1][j - 1] >= arr1[i - 1][j - 1] <= arr1[i][j - 1]:
            prev[i][j] = 'U'
        elif arr1[i][j - 1] <= arr1[i + 1][j - 1]:
            prev[i][j] = 'L'
        else:
            prev[i][j] = 'D'

min1 = arr1[1][n]
for i in range(1, m + 1):
    if arr1[i][n] < min1:
        min1 = arr1[i][n]
        ind = i

i = ind
j = n
path[j - 1] = ind

while j > 1:
    if prev[i][j] == 'U':
        i -= 1
    elif prev[i][j] == 'D':
        i += 1
    else:
        path[j - 2] = i
        j -= 1

print(path, '\n', min1)
