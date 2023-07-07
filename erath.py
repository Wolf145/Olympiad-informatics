a = int(input())
arr = [i for i in range(1, a + 1)]
for i in range(2, int(a ** 0.5) + 1):
    for j in range(i ** 2, a + 1):
        if (arr[j - 1] != 0) and j % i == 0:
            arr[j - 1] = 0
for i in arr:
    if i != 0 and i != 1:
        print(i, end=' ')
