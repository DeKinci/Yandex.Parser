from selenium import webdriver


def scrap(url):
    browser = __start_browser()

    page = __scrap_page(browser, url)

    __write_page(page, 'last_scrap')
    __close_browser(browser)
    return page


def scrap_all(items):
    browser = __start_browser()
    pages = []

    for item in items:
        page = __scrap_page(browser, item.url)
        pages.append(page)

    __close_browser(browser)
    return pages


def __start_browser():
    print('Starting headless browser...')
    options = webdriver.ChromeOptions()
    # options.add_argument('headless')
    browser = webdriver.Chrome('chrome/chromedriver.exe', options=options)
    browser.implicitly_wait(30)
    print('Browser started')
    return browser


def __close_browser(browser):
    print("Closing chrome")
    browser.quit()


def __scrap_page(browser, url):
    print('Opening url: ' + url)
    browser.get(url)
    print('Url opened')
    return browser.page_source


def __write_page(page, name):
    with open('output/' + name + '.html', 'wb') as of:
        of.write(str(page).encode('utf-8'))
