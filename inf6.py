min1 = 30001
for i in range(int(input())):
    a = int(input())
    if (a % 2 == 0) and (a < min1):
        min1 = a
print(min1)
