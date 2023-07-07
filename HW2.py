min1 = 30000
for i in range(int(input())):
    a = int(input())
    if (a < min1) and (a % 3 == 0):
        min1 = a
print(min1)
