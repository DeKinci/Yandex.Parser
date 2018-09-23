from collections import namedtuple
from bs4 import BeautifulSoup
import re

Item = namedtuple('Item', 'url title path preview')


def parse(html_content):
    soup = BeautifulSoup(html_content, 'lxml')
    datalist = soup.find_all('li', {'class': 'serp-item'})

    result = []
    for itemRaw in datalist:
        h2 = itemRaw.find('h2')
        if h2 is None:
            continue
        header = h2.find('a')
        if header is None:
            continue

        url = header.get('href')
        if not url.startswith('http'):
            url = 'http:' + url

        title = header.text
        path = itemRaw.find('div', {'class': 'path organic__path'}).text

        previewRaw = itemRaw.find('div', {'class': 'text-container typo typo_text_m typo_line_m organic__text'})
        preview = ''
        if previewRaw is not None:
            preview = previewRaw.text
        else:
            previewRaw = itemRaw.find('span', {'class': 'extended-text__full'})
            if previewRaw is not None:
                preview = previewRaw.text

        result.append(Item(url, title, path, preview))

    return result


def item2string(item):
    result = ''
    result += item.url + '\n'
    result += item.title + '\n'
    result += item.path + '\n'
    result += item.preview + '\n'
    result += '------------***------------\n'
    return result


def get_encoding(html_content):
    soup = BeautifulSoup(html_content, 'lxml')
    encod = soup.meta.get('charset')
    if encod is None:
        encod = soup.meta.get('content-type')
        if encod is None:
            content = soup.meta.get('content')
            match = re.search('charset=(.*)', content)
            if match:
                encod = match.group(1)
            else:
                encod = 'utf-8'
    return encod
