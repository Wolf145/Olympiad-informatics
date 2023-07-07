n, k = (int(i) for i in input().split())
arr = [[0 for i in range(n + 2)] for j in range(n + 2)]
arr1 = [[0 for i in range(n + 2)] for j in range(n + 2)]
arr2 = [[0 for i in range(n + 2)] for j in range(n + 2)]

for i in range(1, n + 1):
    o = input().split()
    for j in range(1, n + 1):
        arr[i][j] = int(o[j - 1])

arr1[1][1] = arr[1][1]

for l in range(2, k + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if arr1[i][j - 1] != 0 or arr1[i - 1][j] != 0 or arr1[i + 1][j] != 0 or arr1[i][j + 1] != 0:
                arr2[i][j] += max(arr1[i + 1][j], arr1[i - 1][j], arr1[i][j + 1], arr1[i][j - 1]) + arr[i][j]
            else:
                arr2[i][j] = 0

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            arr1[i][j] = arr2[i][j]

max1 = 0
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if arr2[i][j] > max1:
            max1 = arr2[i][j]
print(max1)
