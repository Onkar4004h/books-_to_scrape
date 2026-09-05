from bs4 import BeautifulSoup


with open('websites/books.html') as html_doc:
    soup = BeautifulSoup(html_doc, 'html.parser')
row=soup.find_all('div',class_='row')
print(row)
# side_row=row.find('aside',class_='sidebar col-sm-4 col-md-3')
# print(side_row)
# inner_row=side_row.find('div',class_='side_categories')
# ul=inner_row.find('ul',class_='nav nav-list')
# print(ul)
    