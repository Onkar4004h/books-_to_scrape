from bs4 import BeautifulSoup


with open('websites/books.html') as html_doc:
    soup = BeautifulSoup(html_doc, 'html.parser')
categories= soup.find('ul',class_="nav nav-list")

first_li=categories.find('li')
nested_ul = first_li.find('ul')
for x in nested_ul.find_all('li'):
    print(x.get_text(" ",strip=True))