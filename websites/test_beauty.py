from bs4 import BeautifulSoup
import requests
# with open("websites/index.html") as fp:
#     soup=BeautifulSoup(fp, 'html.parser')
#     # print(soup)
# link = soup.find('p')
# print(link)
html_text = requests.get('https://beautiful-soup-4.readthedocs.io/en/latest/#making-the-soup')
print(html_text.pre)