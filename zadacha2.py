#'https://stepic.org/media/attachments/course67/3.6.3/'
import requests
url = 'https://stepic.org/media/attachments/course67/3.6.3/' + requests.get(open('dataset_3378_3.txt', 'r').readlines()[0].strip()).text
while 'We' not in requests.get(url).text:
    url = 'https://stepic.org/media/attachments/course67/3.6.3/' + requests.get(url).text
open('output for zadacha2.txt', 'w').writelines(requests.get(url).text)
