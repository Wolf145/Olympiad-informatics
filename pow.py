n = int(input())
count = 0
d = 3
while n % 2 == 0:
    count += 1
    n //= 2
print(2, count)
while n != 1:
    count = 0
    while n % d == 0:
        count += 1
        n //= d
    if count != 0:
        print(d, count)
    d += 2
