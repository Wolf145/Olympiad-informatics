n, m = map(int, input().split())

d = {'W':'B', 'B':'W'}

arr1 = [[i for i in input()] for j in range(n)]

arr2 = [[i for i in input()] for j in range(n)]

count = 0

for i in range(n):
    for j in range(m):
        if (d[arr2[i][j]] != arr1[i][j]):
            count += 1

print(count)