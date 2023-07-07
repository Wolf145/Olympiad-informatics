a, b, n = map(int, input().split())
list1 = [0, a, b]# list1[0] = gcd(a, b), list[1] = a, ;list1[2] = b

def floor(x):
    if (0 < x - int(x) < 1) or (-1 > x - int(x) > 0):
        return int(x)
    else:
        return int(x)

def roof(x):
    if (0 < x - int(x) < 1) or (-1 > x - int(x) > 0):
        return int(x) + 1
    else:
        return int(x)

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

solution = gcd_ex(list1[1], list1[2])

kmax = floor(n * solution[2] / list1[1])
kmin = roof(n * solution[1] / b)

print(solution[0], solution[1], solution[2])
print(kmin, n * solution[1] + list1[2] * kmin, n * solution[2] - list1[1] * kmin)
print(kmax, n * solution[1] + list1[2] * kmax, n * solution[2] - list1[1] * kmax)
