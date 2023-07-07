e, f = (int(i) for i in input().split())
wt = f - e
n = int(input())
ar = []
for i in range(n):
    ar.append([int(j) for j in input().split()])

print(ar)

Pmax, Pmin = [0 for i in range(wt + 1)], [0 for i in range(wt + 1)]

for wi in range(1, wt + 1):
    Pmax[wi] = -1000000000
    Pmin[wi] = 1000000000
    for j in range(n):
        if wi >= ar[j][1]:
            Pmax[wi] = max(Pmax[wi], ar[j][0] + Pmax[wi - ar[j][1]])
            Pmin[wi] = min(Pmin[wi], ar[j][0] + Pmin[wi - ar[j][1]])

print(Pmin[wt], Pmax[wt])
