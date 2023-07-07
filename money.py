def money(n, i = 1):
    new = n // (i * 10)
    old = n % (i * 10)
    if new != 0:
        money(new, i + 1)
    if old != 0:
        print(old, i - 1)
money(int(input()))
