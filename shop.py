n, k = int(input()), int(input())

arr = [[0 for j in range(n + 3)] for i in range(k + 1)]

arr[1][0] = 1

for i in range(1, k + 1):
    for j in range(1, n + 2):
        arr[j][i] = arr[j - 1][i - 1] + arr[j + 1][i - 1]

print(arr[n + 1][k])
