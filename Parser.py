from collections import namedtuple

from bs4 import BeautifulSoup

Item = namedtuple('Item', 'url title path preview')


def parse(html_content):
    soup = BeautifulSoup(html_content, 'lxml')

    datalist = soup.find_all('li', {'class': 'serp-item'})

    result = []
    for itemRaw in datalist:

        header = itemRaw.find('h2').find('a')
        url = header.get('href')
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
    result += '------------***------------'
    return result
