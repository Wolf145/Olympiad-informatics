#[1]
'''
def f(n):
    global arr
    if (n not in arr.keys()):
        if (n == 3):
            arr[n] = 1
        elif (n < 3):
            arr[n] = 0
        else:
            arr[n] = f(n // 2) + f(n // 2 + n % 2)
    return arr[n]

n = int(input())

arr = {}

print(f(n))
'''

#[2].1
'''
def dfs(from1, mat):
    global count
    global used

    used[from1] = 1

    for i in range(len(mat[from1])):
        if (not used[mat[from1][i]]):
            count += 1
            dfs(mat[from1][i], mat)

arr = [[] for i in range(10 ** 6 + 1)]
used = [0] * ((10 ** 6) + 1)

for i in range(int(input())):
    a, b = map(int, input().split())
    arr[b].append(a)

count = 1

dfs(int(input()), arr)

print(count)
'''

#[2].2
'''
def f(k, mat):
    count = 1

    for i in mat:
        if i[1] == k:
            count += f(i[0], mat)
    return count

n = int(input())

ar = [[int(i) for i in input().split()] for j in range(n)]

print(f(int(input()), ar))
'''