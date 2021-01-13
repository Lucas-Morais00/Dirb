import requests

url = "https://www.terra.com.br/"

wordlist = open('wordlists_common.txt','r')
linhas = wordlist.readlines()
lista = []

lista = [x.strip() for x in linhas]

for linha in lista:
    r = requests.get(url + linha)
    print(linha + " " + str(r.status_code))
    if r.status_code != 404:
        print("-------------------------------------------")




