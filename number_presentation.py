with open('in.txt', 'r') as in1:
    a = int(in1.readline())
    del1 = a
    if a % 2 == 0:
        del1 = 2
    else:
        i = 3
        while i * i <= a:
            if a % i == 0:
                del1 = i
                break
            i += 2
        out1 = str(a // del1) + ' ' + str((del1 - 1) * a // del1)
        with open('out.txt', 'w') as out:
            out.write(out1)
