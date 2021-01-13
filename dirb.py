#You need to download the .txt file and have it in the same
#directory

#This program may take a while to finish all words

#pip install requests
import requests

#enter your URL here with a / after the last character
url = ""

wordlist = open('wordlists_common.txt','r')
lines = wordlist.readlines()
words = []

words = [x.strip() for x in lines]

for line in words:
    r = requests.get(url + line)
    print(line + " " + str(r.status_code))
    if r.status_code != 404:
        print("-------------------------- You found something! --------------------------")



