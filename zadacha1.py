import requests
read = open('dataset_3378_2.txt', 'r').readlines()
open('output for zadacha1.txt', 'w').writelines(str(len(requests.get(read[0].strip()).text.splitlines())))
