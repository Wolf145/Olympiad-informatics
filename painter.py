n, m = map(int, input().split())
arr = [[0 for i in range(n)] for j in range(m)]

count = n * m

for i in range(int(input())):
    xs, ys, xf, yf = map(int, input().split())
    for y in range(ys, yf, 1):
        for x in range(xs, xf, 1):
            if (not arr[x][y]):
                arr[x][y] = 1
                count -= 1

print(count)