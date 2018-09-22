from Parser import parse, item2string

with open('test/test.html', 'r', encoding='utf-8') as file:
    data = file.read()

items = parse(data)

for item in items:
    print(item2string(item))
