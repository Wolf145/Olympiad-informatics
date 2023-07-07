inp = int(input())
count = 0
while inp != 6174:
    k = ''
    while inp < 1000:
        inp *= 10
    str1 = []
    for i in str(inp):
        str1.append(int(i))
    str1 = sorted(str1)
    for i in str1:
        k += str(i)
    str1 = int(k)
    str2 = int(k[::-1])
    inp = str2 - str1
    count += 1

print(6174, '\n', count, sep='')
