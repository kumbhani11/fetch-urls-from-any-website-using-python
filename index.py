from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import re
req = Request("https://www.python.org/")
html_page = urlopen(req)

soup = BeautifulSoup(html_page, "lxml")

links = []
for link in soup.findAll('a'):
    links.append(link.get('href'))

for i in range (0, (len(links))):
    print(links[i])
print('Total link found =' + str(len(links)))
