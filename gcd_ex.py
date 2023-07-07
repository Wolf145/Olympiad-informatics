a, b = (int(input()) for i in range(2))
list1 = [0, a, b]# list1[0] = gcd(a, b), list[1] = a, ;list1[2] = b

def sign(x):
    if x < 0:
        return -1
    if x == 0:
        return 0
    if x > 1:
        return 1

def gcd_ex(x, y):
    sc = [0, 0, 0]
    if y == 0:
        sc[0] = x
        sc[1] = 1
        sc[2] = 0
    else:
        sc = gcd_ex(y, x % y)
        t = sc[1] - (x // y) * sc[2]
        sc[1] = sc[2]
        sc[2] = t
    return sc

solution = gcd_ex(abs(list1[1]), abs(list1[2]))
print(solution[0], sign(list1[1]) * solution[1], sign(list1[2]) * solution[2])
