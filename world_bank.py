import csv
from urllib.request import urlopen

from bs4 import BeautifulSoup

def get_country(country_code):
    html = urlopen(
        'http://api.worldbank.org/v2/countries/{}'.format(country_code)
    )
    soup = BeautifulSoup(html, 'xml')
    country_name = soup.find('wb:name')
    region = soup.find('wb:region')
    income_level = soup.find('wb:incomeLevel')
    l = [country_name, region, income_level]
    for m in l:
        print(m.get_text())


if __name__ == '__main__':
    # country_iso_codes.csv is in the teacher's notes
    # otherwise the string 'ETH' can be used
    file = open('country_iso_codes.csv', 'r')
    iso_codes = csv.reader(file, delimiter=',')

    for code in iso_codes:
        get_country(code[0])
