n = int(input())
arr = [[0 for i in range(7)] for j in range(8)]
arr1 = [[0 for i in range(7)] for j in range(8)]
sum1 = 0

for i in range(2, 5):
    for j in range(2, 5):
        arr[i][j] = 1

arr[4][3] = 0

for k in range(n - 1):
    for i in range(2, 6):
        for j in range(2, 5):
            arr1[i][j] += arr[i + 2][j + 1] + arr[i + 2][j - 1] + arr[i - 2][j + 1] + arr[i - 2][j - 1] + arr[i - 1][j + 2] + arr[i + 1][j + 2] + arr[i - 1][j - 2] + arr[i + 1][j - 2]
    
    arr1[5][2] = 0
    arr1[5][4] = 0
    
    for i in range(2, 6):
        for j in range(2, 5):
            arr[i][j] = arr1[i][j]

for i in range(2, 6):
    for j in range(2, 5):
        sum1 += arr[i][j]

print(sum1)

