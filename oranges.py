def gcd(a, b):
    if a < b:
        a, b = b, a

    if b == 0:
        return a

    else:
        return gcd(b, a % b)

with open('in.txt', 'r') as in1:
    friends, orang = (int(i) for i in in1.readline().split())

with open('out.txt', 'w') as out:
    if friends < orang:
        friends, orang = orang, friends
    out.write(str(orang // gcd(friends, orang)))
    
