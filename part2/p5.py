import requests

from bs4 import BeautifulSoup

url = "http://quotes.toscrape.com/"
page = requests.get(url)
soup = BeautifulSoup(page.text, "html.parser")

# p = soup.select("p")
# print(p)

# text = soup.select(".text")
# print(text)

# header = soup.select("#header")

# a = soup.select("div.container a")
# print(a)

href = soup.select("[href^='https://']")
print(href)

ctext = soup.select("[class*='text']")
print(ctext)
