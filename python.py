# Import libraries -------------------#
from bs4 import BeautifulSoup
soup = BeautifulSoup(page.content, 'html.parser')
#-------------------------------------#

print(soup.prettify())

ebay_url = "https://www.ebay.ca/"
kijiji_url = "https://www.kijiji.ca/"
grailed_url = "https://www.grailed.com/"

print(ebay_url)
