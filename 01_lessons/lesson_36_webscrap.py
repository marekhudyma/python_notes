# pip install requests
# pip install lxml
# pip install bs4


import requests
import bs4

result = requests.get('https://en.wikipedia.org/wiki/Grace_Hopper')
type(result)
print(result.text)

soup = bs4.BeautifulSoup(result.text, 'lxml')
print(soup.select('title')) # [<title>Welcome to Python.org</title>]

print(soup.select('.mw-heading'))