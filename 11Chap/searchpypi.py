'''
Project: Opening All Search Results
search results page for the Python Package Index at https://pypi.org/.
'''
#! python3

import sys
import requests
import webbrowser
from bs4 import BeautifulSoup

print('searching.....')

RES = requests.get('https://pypi.org/search/?q=' + ' '.join(sys.argv[1:]))
RES.raise_for_status()

SOUP = BeautifulSoup(RES.text, 'html.parser')
LINK_ELEMS = SOUP.select('.package-snippet')
print(len(LINK_ELEMS))

for i in range(5):
    URL_TO_OPEN = 'https://pypi.org' + LINK_ELEMS[i].get('href')
    print('opening...', URL_TO_OPEN)
    webbrowser.open(URL_TO_OPEN)
