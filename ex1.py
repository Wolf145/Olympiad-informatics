read = open('dataset_3363_2.txt', 'r').readline()
numbers = '0123456789'
count1, count2 = -1, 0
with open('output1.txt', 'w') as output:
    while count2 < len(read):
        count1 += 1
        count2 += 1
        if (read[count1] in numbers) and (read[count1 - 1] not in numbers) and (read[count2] not in numbers):
            output.write(read[count1 - 1] * int(read[count1]))
        if (read[count1] in numbers) and (read[count2] in numbers):
            output.write(read[count1 - 1] * int(read[count1] + read[count2]))
        else:
            continue
