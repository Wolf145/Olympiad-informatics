a, summ, Y_or_N = int(input()), 0, 'NO'
for i in range(a):
    b = int(input())
    summ += b
    if b >= 60:
        Y_or_N = 'YES'
print(round(summ / a, 1), '\n', Y_or_N, sep='')
