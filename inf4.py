sum1 = 0
a = int(input())
while a != 0:
    if (a % 6 == 0) and (a % 10 == 4):
        sum1 += a
    a = int(input())
print(sum1)
