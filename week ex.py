read, dict1 = [i.strip().split() for i in open('dataset_3380_5.txt', 'r').readlines()], {'1': [0], '2': [0], '3': [0], '4': [0], '5': [0], '6': [0], '7': [0], '8': [0], '9': [0], '10': [0], '11': [0]}
for i in range(len(read)):
    dict1[read[i][0]].append(int(read[i][2]))
sum1 = 0
with open('output.txt', 'w') as output1:
    for i in dict1.keys():
        if len(dict1[i]) == 1:
            output1.write(i + ' -' + '\n')
        else:
            for j in range(len(dict1[i])):
                sum1 += dict1[i][j]
            output1.write(i + ' ' + str(sum1 / j) + '\n')
            sum1 = 0
