N, K = (int(i) for i in input().split())
min1 = 2 * (10 ** 9)
max1 = -2 * (10 ** 9)
for i in range(N):
    a = int(input())
    if a < min1:
        min1 = a
    if a > max1:
        max1 = a
print(max1 - min1)
