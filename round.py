def round1(x, a):
    res = [i for i in str(x)]
    ans = ''
    for i in range(len(res)):
        ans += res[i]
        if res[i] == '.':
            break
    res1 = [int(j) for j in res[(i + 1):]]
    if a >= len(res1):
        return x
    for i in range(len(res1)):
        if i == a - 1:
            if res1[i + 1] >= 5:
                ans += str(res1[i] + 1)
            else:
                ans += str(res1[i])
            return float(ans)
        ans += str(res1[i])
print(round1(3.1555749856747509248564072654525, 10))
