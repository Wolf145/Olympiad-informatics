arr = list()
for i in range(int(input())):
    arr.append(int(input()))
rost = int(input())
for i in range(1, len(arr)):
    if arr[i - 1] < rost > arr[i]:
        print(i)
        break
