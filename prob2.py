num = int(input())
chisla = input().split()
for i in range(len(chisla)):
	chisla[i] = int(chisla[i])
string = ''
if len(chisla) == num:
    for i in sorted(chisla):
        string += (str(i) + ' ')
    print(string[:len(string) - 1])
