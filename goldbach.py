a = int(input())
arr = [i for i in range(1, a + 1)]
arr[0] = 0
ans = str(a) + '='
count = 0

if a > 2:

    for i in range(2, int(a ** 0.5) + 1):

        for j in range(i ** 2, a + 1):

            if (arr[j - 1] != 0) and j % i == 0:
                arr[j - 1] = 0


    for i in arr:

        if i > a // 2:
            break


        elif i != 0 and a - i != 0 and (a - i in arr):
            ans += str(i) + '+' + str(a - i) + '='
            count += 1

print(ans[:len(ans) - 1])
print(count)
