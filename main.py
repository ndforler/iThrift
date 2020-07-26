# Import libraries -------------------#
#you need to properly import requests and BeautifulSoup on to your computer
from bs4 import BeautifulSoup
import requests
import csv

with open('index.html') as html_file:
    soup = BeautifulSoup(html_file, 'lxml')

source1 = requests.get('https://ebay.ca/').text

soup = BeautifulSoup(source1, 'lxml')

csv_file = open('cms_scrape', 'w')

csv_writer = cvs.writer(csv_file)
csv_writer.writerow(['brandname', 'size', 'price', 'image'])
csv_write

for article in soup.find_all('article')
    brandname = article.div.text
    print headline

match = soup.titletext
print(match)
soup = BeautifulSoup(page.content, 'html.parser')

# we need to figure out how to link the search bar to the search value
search =

# link the search value into each url in the correct position

ebay = requests.get(ebay_url)
kijiji = requests.get(kijiji_url)
grailed = requests.get(grailed_url)
#testing the url

for span in soup.find_all(class_='amt'):
    print(span.get_text())
