read, dict1, update_dict1 = [], dict(), dict()
with open('dataset_3363_3.txt', 'r') as input1:
    for i in input1:
        for j in i.split():
            read.append(j.strip().lower())
with open('output2.txt', 'w') as output1:
    count = read.count(read[0])
    for key in read:
        if count <= read.count(key):
            count = read.count(key)
            set(dict1).add(key)
            dict1[key] = count
    for key, value in dict1.items():
        if count == value:
            set(update_dict1).add(key)
            update_dict1[key] = count
            str1 = key
    if len(update_dict1) == 1:
        output1.write(str1 + ' ' + str(count))
    if len(update_dict1) > 1:
        for key in update_dict1.keys():
            if str1 > key:
                str1 = key
        output1.write(str1 + ' ' + str(count))
    
