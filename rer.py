M, N =(int(input()) for i in range(2))
def f(m, n):
    if m > n:
        m, n = n, m
    if m == 1:
        return n
    if m == 0:
        return 0
    return n // m + f(n % m, m)

print(f(M, N))
