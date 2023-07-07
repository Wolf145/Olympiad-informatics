read = []
with open('dataset_3363_4.txt', 'r') as input1:
    for i in input1:
        read.append(i.strip().split(';'))
dict1, sredarif, math, phys, rus = dict(), 0, 0, 0, 0
for i in range(len(read)):
    for j in range(1, 4):
        sredarif += int(read[i][j])
    set(dict1).add(read[i][0])
    dict1[read[i][0]] = sredarif / 3
    sredarif = 0
    math += int(read[i][1])
    phys += int(read[i][2])
    rus += int(read[i][3])
with open('output3.txt', 'w') as output1:
    for i in dict1.values():
        output1.write(str(i)+'\n')
    output1.write(str(math / len(read)) + '\t' + str(phys / len(read)) + '\t' + str(rus / len(read)))
    
