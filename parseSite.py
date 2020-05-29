import requests
from bs4 import BeautifulSoup as BS

r = requests.get('')
html = BS(r.content, '')

for el in html.select(''):
    title = el.select('')
    print(title[0].text)
