
from bs4 import BeautifulSoup
from urllib.request import urlopen

quote_page = "https://www.w3schools.com/"
page = urlopen(quote_page)
soup = BeautifulSoup(page, 'html.parser')
tutorials_list = soup.findAll(attrs={'class': 'w3-bar-item w3-button'})
file = open("webText.txt","a")

for tutorials in tutorials_list:
    name = tutorials.text.strip()
    file.write(name + "\n")

print("Data extracted successfully!")
file.close()

