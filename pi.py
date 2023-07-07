sum1, n, num = 0, 1, 1
while True:
    if n % 2 != 0:
        sum1 += 1 / num
    if n % 2 == 0:
        sum1 -= 1 / num
    n += 1
    num += 2
    print(sum1 * 4)
    
