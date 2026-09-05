from bs4 import BeautifulSoup


with open('websites/books.html') as html_doc:
    soup = BeautifulSoup(html_doc, 'html.parser')
all_divs= soup.find_all('div')[0]
print(all_divs.find('small').text)