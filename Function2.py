def F(a, b, c):
    global D
    if ((a, b, c) not in D.keys()):
        if (a <= 0 or b <= 0 or c <= 0):
            D[(a, b, c)] = 1
        elif (a > 20 or b > 20 or c > 20):
            D[(a, b, c)] = F(20, 20, 20)
        elif(a < b and b < c):
            D[(a, b, c)] = F(a, b, c-1) + F(a, b-1, c-1) - F(a, b-1, c)
        else:
            D[(a, b, c)] = F(a-1, b, c) + F(a-1, b-1, c) + F(a-1, b, c-1) - F(a-1, b-1, c-1)
    return D[(a, b, c)]


a, b, c = map(int, input().split())

D = {}
F(a, b, c)

print(D[(a, b, c)])