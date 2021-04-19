import time

from selenium import webdriver


def get_html():
    # Запускаем браузер, авторизуемся и получаем новый Auth-Token; Bearer-Token и записываем или обновляем в файле

    driver = webdriver.Chrome('/Users/macbookpro/Documents/AvtoParse/MANHEIM/chromedriver')
    driver.get('https://www.manheim.com')
    time.sleep(3)

    driver.find_element_by_xpath('//*[@id="uhf-header--container"]/header/div[4]/span[2]/span[1]/a').click()
    time.sleep(3)

    login_ = driver.find_element_by_xpath('//*[@id="user_username"]')
    password_ = driver.find_element_by_xpath('//*[@id="user_password"]')
    btn = driver.find_element_by_xpath('//*[@id="submit"]')

    login_.send_keys('vasush59')
    password_.send_keys('vashak159')
    time.sleep(3)
    btn.click()

    time.sleep(3)

    html = driver.page_source
    return html


def get_token_and_bear():
    html = get_html()

    auth_token = html.split('id="postLoginComponent" data-auth-tkt="')[1].split('"')[0]
    bear_token = html.split('data-bearer-token="')[1].split('"')[0]

    print(auth_token)
    print(bear_token)

    with open('auth_data.txt', 'w') as file:
        file.write(f'{auth_token}:{bear_token}')
    file.close()


get_token_and_bear()
