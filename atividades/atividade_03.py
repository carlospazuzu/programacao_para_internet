import requests, re
from bs4 import BeautifulSoup

print('Digite a pagina que deseja capturar os links: ', end='')

url = input()

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

f = open('links.txt', 'w+')

for link in soup.findAll('a', attrs={'href': re.compile('^http://')}):
    f.write(link.get('href') + '\n')

f.close()
