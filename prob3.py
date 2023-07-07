primeri = [input().split() for i in range(int(input()))]
otvet = [[] for i in range(len(primeri))]
def nod(a, b):
    NOD1, NOD2 = a, b
    while NOD1 != 0 and NOD2 != 0:
        if NOD1 > NOD2:
            NOD1 %= NOD2
        else:
            NOD2 %= NOD1
    NOD = NOD1 + NOD2
    a //= NOD
    b //= NOD
    return a, b
for i in range(len(primeri)):
    primeri[i][0], primeri[i][1], primeri[i][3], primeri[i][4] = int(primeri[i][0]), int(primeri[i][1]), int(primeri[i][3]), int(primeri[i][4])
    primeri[i][0], primeri[i][1] = nod(primeri[i][0], primeri[i][1])
    primeri[i][3], primeri[i][4] = nod(primeri[i][3], primeri[i][4])
    if primeri[i][2] == '+':
        if primeri[i][1] != primeri[i][4]:
            chislo1 = primeri[i][0] * primeri[i][4] + primeri[i][3] * primeri[i][1]
            chislo2 = primeri[i][1] * primeri[i][4]
        if primeri[i][1] == primeri[i][4]:
            chislo1 = primeri[i][0] + primeri[i][3]
            chislo2 = primeri[i][1]
    if primeri[i][2] == '-':
        if primeri[i][1] != primeri[i][4]:
            chislo1 = primeri[i][0] * primeri[i][4] - primeri[i][3] * primeri[i][1]
            chislo2 = primeri[i][1] * primeri[i][4]
        if primeri[i][1] == primeri[i][4]:
            chislo1 = primeri[i][0] - primeri[i][3]
            chislo2 = primeri[i][1]
    if primeri[i][2] == ':':
        chislo1 = primeri[i][0] * primeri[i][4]
        chislo2 = primeri[i][1] * primeri[i][3]
    if primeri[i][2] == '*':
        chislo1 = primeri[i][0] * primeri[i][3]
        chislo2 = primeri[i][1] * primeri[i][4]
    chislo1, chislo2 = nod(chislo1, chislo2)
    if chislo1 < 0 and chislo2 < 0:
        chislo1, chislo2 = abs(chislo1), abs(chislo2)
    if chislo2 < 0:
        chislo1, chislo2 = -chislo1, abs(chislo2)
    otvet[i].append(chislo1)
    otvet[i].append(chislo2)
output = ''
for i in range(len(otvet)):
    output += str(otvet[i][0]) + ' ' + str(otvet[i][1]) + '\n'
print(output)
