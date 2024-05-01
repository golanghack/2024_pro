from urllib.request import urlopen
from bs4 import BeautifulSoup as bs 

html = urlopen('http://www.pythonscraping.com/pages/warandpeace.html')
get = bs(html.read(), 'html.parser')

green_context = {'class': 'green', }
name_list = get.find_all('span', green_context)

for index, name in enumerate(name_list):
    print(index, name.get_text())
