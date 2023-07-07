list1= list()
for i in range(int(input())):
    list1.append([int(j) for j in input().split()])
list2 = [[] for i in range(len(list1))]
for i in range(len(list1)):
    for j in range(len(list1[i])):
        if list1[i].count(list1[i][j]) > 1:
            list2[i].append('YES')
        else:
            list2[i].append('NO')
for i in list2:
    if i.count('YES') >= i.count('NO'):
        print('YES')
    else:
        print('NO')
