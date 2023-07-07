max1 = 0
for i in range(int(input())):
    a = int(input())
    if (a % 5 == 0) and (a > max1):
        max1 = a
print(max1)
