import requests
from bs4 import BeautifulSoup

useragent = input("USERAGENT: ")
secret_key = input("SKEY: ")
tgid = input("TGID: ")
api_key = input("APIKEY: ")

while True:
    headers = {
        "User-Agent": useragent
    }
    r = requests.get("https://www.nationstates.net/cgi-bin/api.cgi?q=newnations", headers=headers)
    soup = BeautifulSoup(r.text, "lxml")
    text_file = open("nation_list.txt", "rw")
    output = soup.nations.string
    output = output.replace(',', '\n')
    text_file.write(output)

    # recruitment loop

    # i should be no more than ten to make sure you're hitting fresh-ish nations
    while i < 10:
        nation = text_file.readline(i)
        params = {
            "a": "sendTG",
            "client": api_key
            "to": nation
            "tgid": tgid
            "key": secret_key
        }
        requests.get("https://www.nationstates.net/cgi-bin/api.cgi", headers=headers, params=params)
