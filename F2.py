def F(a, b, c):
    global D
    if (a <= 0 or b <= 0 or c <= 0):
        return 1
    elif (a > 20 or b > 20 or c > 20):
        return F(20, 20, 20)
    elif (D[a][b][c] == -1):
        if (a < b and b < c):
            D[a][b][c] = F(a, b, c - 1) + F(a, b - 1, c - 1) - F(a, b - 1, c)
        else:
            D[a][b][c] = F(a-1, b, c) + F(a-1, b-1, c) + F(a-1, b, c-1) - F(a-1, b-1, c-1)

    return D[a][b][c]

D = [[[-1 for i in range(21)] for j in range(21)] for k in range(21)]

a, b, c = map(int, input().split())

print(F(a, b, c))

