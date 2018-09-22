from Parser import parse

with open('test/test.html', 'r', encoding='utf-8') as file:
    data = file.read()
parse(data)
