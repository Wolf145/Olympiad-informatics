x, summ = int(input()), 0
while x != 0:
    if (x % 10 == 2) and (x % 7 == 0):
        summ += x
    x = int(input())
print(summ)
