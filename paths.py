a, b = map(int, input().split())
arr = [[int(i) for i in input().split()] for j in range(a)]
arr1 = [[0 for i in range(b)] for j in range(a)]
arr1[0][0] = 1

for i in range(a):
    for j in range(b):
        if arr[i][j] != 0:
            if i + arr[i][j] <= a - 1:
                arr1[i + arr[i][j]][j] += arr1[i][j]
            if j + arr[i][j] <= b - 1:
                arr1[i][j + arr[i][j]] += arr1[i][j]
print(arr1[a - 1][b - 1])
