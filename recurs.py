def f(n):
    global c
    c = 1
    if n >= 1:
        c = 2 + f(n - 1) + f(n - 3)
    return(c)
    
print(f(int(input())))
