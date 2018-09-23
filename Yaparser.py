from Parser import parse, item2string
from Scrapper import scrap, scrap_all
import os
import re

query = input("Search: ")
url = "https://yandex.ru/yandsearch?text=" + query.replace(" ", "%20%20")

query_dir = query
counter = 1
while os.path.exists(query_dir):
    query_dir = query + ' (' + str(counter) + ')'
    counter += 1
os.makedirs(query_dir)

page = scrap(url)

with open(query_dir + '/query.html', 'wb') as of:
    of.write(str(page).encode('utf-8'))

items = parse(page)
with open(query_dir + '/result.txt', 'wb') as of:
    for item in items:
        of.write(item2string(item).encode('utf-8'))

print('Scrapping results')
result_pages = scrap_all(items)

print('Saving results')
for result_page in result_pages:
    search_name = items[result_pages.index(result_page)].title
    search_name = re.sub('[|/:*?"<>+%\\\]', '', search_name)
    file_name = query_dir + '/' + search_name

    print('Checking name ' + file_name)
    unique_file_name = file_name
    counter = 1

    while os.path.exists(unique_file_name + '.html'):
        unique_file_name = file_name + ' (' + str(counter) + ')'
        counter += 1
        print('Checking name ' + unique_file_name)

    unique_file_name += '.html'
    print('Writing to ' + unique_file_name)

    with open(unique_file_name, 'wb') as of:
        of.write(str(result_page).encode('utf-8'))
    print('File written')
