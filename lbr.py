n, k = int(input()), int(input())
lbr, pat1, pat2 = [[0 for j in range(n + 2)] for i in range(n + 2)], [[0 for j in range(n + 2)] for i in range(n + 2)], [[0 for j in range(n + 2)] for i in range(n + 2)]
for i in range(1, n + 1):
    lbr[i] = [0] + [int(i) for i in input().split()] + [0]

pat1[1][1] = 1

for p in range(k):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if lbr[i][j] == 1:
                pat2[i][j] = 0
            else:
                pat2[i][j] = pat1[i-1][j] + pat1[i+1][j] +pat1[i][j-1] +pat1[i][j+1]
    pat1, pat2 = pat2, pat1

print(pat1[n][n])
