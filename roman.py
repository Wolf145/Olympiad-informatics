def f(x):
    t_c = 1
    f_p = x
    cur_c = 0

    while cur_c <= n - 1:
        if a[cur_c] > x:
            t_c = 0
            break
        if f_p >= a[cur_c]:
            f_p -= a[cur_c]
            cur_c += 1
        else:
            t_c += 1
            f_p = x
    return (t_c != 0) and (t_c <= k)

n, a, k = int(input()), [int(i) for i in input().split()], int(input())

l, r = 0, 10000000000000

while r - l != 1:
    avg = l + (r - l) // 2

    if f(avg):
        r = avg
        
    else:
        l = avg

print(r)
