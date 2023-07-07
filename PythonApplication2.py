N = int(input())
b, c = 0, 0
for i in range(N):
    a = int(input())
    if a < 10 // 2:
        b += 1
    if a == 10:
        c += 1
print(b)
if c > 0:
    print('YES')
else:
    print('NO')