a = int(input())
b = int(input())
c = int(input())
d = 3
a, b, c = a - 1, b - 1, c - 1
e = []
e.append(a)
e.append(b)
e.append(c)
if b != 0:
    for i in range(1000000000000):
        for k in range(1):
            if e[k] == 0:
                break
            e[k] -= 1
        for j in range(1, 3):
            if e[j] == 0:
                break
            e[j] -= 1
    print(d)
else:
    print(d)
    
