from Parser import parse, item2string
from Scrapper import scrap

url = '''http://yandex.ru/yandsearch?text=%D0%9C%D0%B0%D0%B9%D1%81%D0%BA
%D0%B0%D1%8F+%D1%82%D1%80%D0%B0%D0%B2%D0%BA%D0%B0+
%D0%B3%D0%BE%D0%BB%D0%BE%D0%B4%D0%BD%D0%BE%D0%B3%D0%BE+
%D0%BA%D0%BE%D1%80%D0%BC%D0%B8%D1%82&nl=1&lr=2'''
items = parse(scrap(url))

for item in items:
    print(item2string(item))
