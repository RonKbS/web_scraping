from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('https://treehouse-projects.github.io/horse-land/index.html')
soup = BeautifulSoup(html.read(), 'html.parser')

# print(soup.prettify())
# print(soup.title)

# div = soup.find('div', {'class': 'featured'})

# print(div)

# featured_header = soup.find('div', {'class': 'featured'}).h2.get_text()
# use get_text as the last element in the scraping process
# print(featured_header)

# for button in soup.find(attrs={'class': 'button button--primary'}):
#     print(button)
# # OR

# for button in soup.find(class_='button button--primary'):
#     print(button)

for link in soup.find_all('a'):
    print(link.get('href'))
