from bs4 import BeautifulSoup


with open('websites/books.html') as html_doc:
    soup = BeautifulSoup(html_doc, 'html.parser')

