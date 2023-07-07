x, count1 = int(input()), 0
while x != 0:
    if (x % 5 == 0) and (x % 2 == 0):
        count1 += 1
    x = int(input())
print(count1)
