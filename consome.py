import requests
from bs4 import BeautifulSoup
from time import sleep

url = "https://dolarhoje.com/"
response = requests.get(url)

html = BeautifulSoup(response.text, 'html.parser')
lista = []
for i in html.select("#cotacao"):
    valor = i.select("#nacional")
    v = """"""
    v = str(valor)
v = v.replace('[<input id="nacional" type="text" value="', '')
v = v.replace('"/>]', '')
v = v.replace(',', '.')
v = float(v)

