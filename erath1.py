N = int(input())
arr = [i for i in range(2, N + 1)]
arr1 = [i for i in range(2, N + 1)]
n = -1
d = arr[0]

while d * d <= N:
    n += 1
    d = arr[n]
    if d != 0:
        k = 0
        for i in range(n, len(arr1)):
            if arr1[i] == d * d + d * k:
                arr[i] = 0
                k += 1
for i in arr:
    if i != 0:
        print(i)
