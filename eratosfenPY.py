n = int(input())

eratosfen = [1 for i in range (n)]

eratosfen[0] = 0

d = 2
for i in range (d*d, n + 1, d):
    eratosfen[i-1] = 0

d = 3    
while d*d <= n:
    if eratosfen[d-1] != 0:
        for i in range (d*d, n + 1, d):
            eratosfen[i-1] = 0
    d += 2;


for i in range (2, n+1):    
        if eratosfen[i-1] != 0:
            print (i)         
    
