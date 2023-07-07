m, n = map(int, input().split())

count = 0

arr = [[i for i in input()] for j in range(m)]

for j in range(n):
    for i in range(m):
        if (arr[i][j] == '#'):
            if (i == 0 and j == 0
                or i == 0 and j != 0 and arr[i][j - 1] == '.'
                or j == 0 and i != 0 and arr[i - 1][j] == '.'
                or arr[i - 1][j] == arr[i][j - 1] == '.'):
                count += 1
print(count)