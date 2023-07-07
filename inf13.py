count = 1
k = int(input())
a = int(input())
a_prev = a
for i in range(1, k):
    a = int(input())
    if a != a_prev:
        count += 1
    a_prev = a
print(count)
