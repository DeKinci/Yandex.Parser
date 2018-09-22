from selenium import webdriver


def scrap(url):
    print("Starting headless chrome...")
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    driver = webdriver.Chrome('chrome/chromedriver.exe', options=options)

    print("Chrome started, opening url: " + url)
    driver.implicitly_wait(30)
    driver.get(url)

    print("Url opened, saving files")
    driver.save_screenshot("output/last_scrap.png")
    with open('output/last_scrap.html', 'wb') as of:
        of.write(str(driver.page_source).encode('utf-8'))

    print("Closing chrome")
    result = driver.page_source
    driver.quit()
    return result
