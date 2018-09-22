from Parser import parse, item2string
from Scrapper import scrap

query = input("Search: ")
url = "https://yandex.ru/yandsearch?text=" + query.replace(" ", "%20%20")

items = parse(scrap(url))

for item in items:
    print(item2string(item))