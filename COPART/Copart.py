import requests
from loguru import logger


class CopartCarInfo:
    """
    Основной класс для парсинга машин по запросу
    """

    def __init__(self, car_name, from_year):
        self.car = car_name
        self.from_yers = from_year

    def get_car(self):
        cookies = {
            's_fid': '352709014A665B62-038D22B6CEDDB65B',
            's_invisit': 'true',
            's_lv': '1618569187740',
            's_lv_s': 'Less%20than%201%20day',
            's_nr': '1618569187739-Repeat',
            's_ppv': 'public%253AsearchResults%2C33%2C33%2C1736%2C1920%2C590%2C1920%2C1080%2C1%2CP',
            's_pv': 'public%3AsearchResults',
            's_sq': 'copart-g2-us-prod%3D%2526c.%2526a.%2526activitymap.%2526page%253Dpublic%25253AsearchResults%2526link%253D%2525D0%252593%2525D0%2525BE%2525D0%2525B4%2526region%253Dfilters-collapse-1%2526pageIDType%253D1%2526.activitymap%2526.a%2526.c%2526pid%253Dpublic%25253AsearchResults%2526pidt%253D1%2526oid%253Dhttps%25253A%25252F%25252Fwww.copart.com%25252Fru%25252F%252523collapseinside5%2526ot%253DA',
            's_vnum': '1621157058488%26vn%3D2',
            'g2usersessionid': 'f40037d6ef825cec7e96c9bb6aade4be',
            'g2app.searchResultsPageLength': '100',
            'incap_ses_1317_242093': 'Vc8YCVetpWNi9gq8n+xGEvBleWAAAAAAst1pUcxIva99W1YCK2Lfrw==',
            'incap_ses_582_242093': 'qhFUKiGQ3gSw6WAsWK4TCOheeWAAAAAAXxaYAo5+s2ambxuYJ8CRsw==',
            '__gads': 'ID=a3b21b4ce0e31b1f-22645cd626bb0042:T=1618565068:RT=1618565068:S=ALNI_Ma0KWIqLVADIxOKzjHb24DHG2ov0Q',
            's_ppvl': 'public%253Alanding-page-kazakhstan-ru%2C76%2C34%2C1000%2C1920%2C1000%2C1920%2C1080%2C1%2CP',
            's_vi': '[CS]v1|3038F0073956BD66-60001933A0F4DAFB[CE]',
            '_ga_WEF8SZZLJG': 'GS1.1.1618565059.1.1.1618565068.0',
            '_fbp': 'fb.1.1618565059298.1479336970',
            '_ga': 'GA1.2.869404276.1618565059',
            '_gac_UA-90930613-1': '1.1618565059.Cj0KCQjw6-SDBhCMARIsAGbI7UhzLvW6nb7qi8UAMbpQeQNkNM6yoWZA2dsWOgwsflAZ5BpKdWR5KHYaAvFoEALw_wcB',
            '_gcl_aw': 'GCL.1618565059.Cj0KCQjw6-SDBhCMARIsAGbI7UhzLvW6nb7qi8UAMbpQeQNkNM6yoWZA2dsWOgwsflAZ5BpKdWR5KHYaAvFoEALw_wcB',
            '_gid': 'GA1.2.557025786.1618565059',
            's_campaign': 'ppc%3Ag%3Aintl_kazakhstan%3Arussian%3Acar',
            's_ev96': 'Cj0KCQjw6-SDBhCMARIsAGbI7UhzLvW6nb7qi8UAMbpQeQNkNM6yoWZA2dsWOgwsflAZ5BpKdWR5KHYaAvFoEALw_wcB',
            '_gcl_au': '1.1.1409478409.1618565059',
            '_uetsid': '85bb43709e9511eb97c1d18f60a4d622',
            '_uetvid': '0e7024c09a2211eb8a1cadf617c2676e',
            'cid': 'ppc:g:intl_kazakhstan:russian:car',
            'entry_page': 'public%3Alanding-page-kazakhstan-ru',
            's_cc': 'true',
            'g2app.locationInfo': '%7B%22countryCode%22%3A%22KAZ%22%2C%22countryName%22%3A%22Kazakhstan%22%2C%22stateName%22%3A%22Mangghystau%20oblysy%22%2C%22stateCode%22%3A%22%22%2C%22cityName%22%3A%22Omirzaq%22%2C%22latitude%22%3A43.59639%2C%22longitude%22%3A51.255%7D',
            'copartTimezonePref': '%7B%22displayStr%22%3A%22PKT%22%2C%22offset%22%3A5%2C%22dst%22%3Afalse%2C%22windowsTz%22%3A%22Asia%2FKarachi%22%7D',
            'timezone': 'Asia%2FKarachi',
            'G2JSESSIONID': 'EF149D45A0F1AD3F364374136F7610E9-n2',
            'userLang': 'ru',
            '__cfduid': 'dfb4140380f5dcc9172d34f914060958c1618075772',
            'visid_incap_242093': '7UTV1GG7QXOUVuHpLzzHXQrgcWAAAAAAQUIPAAAAAACdE4mCYgZO46NF+xThhuuQ',
        }
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Accept-Language': 'ru',
            'Accept-Encoding': 'gzip, deflate, br',
            'Host': 'www.copart.com',
            'Origin': 'https://www.copart.com',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Safari/605.1.15',
            'Referer': 'https://www.copart.com/ru/lotSearchResults/?free=true&query=toyota',
            'Content-Length': '3580',
            'Connection': 'keep-alive',
            'X-Requested-With': 'XMLHttpRequest',
            'X-XSRF-TOKEN': 'cd8a3474-ff99-4f3b-83bc-85f6bef86536',
        }
        data = {
            'draw': '7',
            'columns[0][data]': '0',
            'columns[0][name]': '',
            'columns[0][searchable]': 'true',
            'columns[0][orderable]': 'false',
            'columns[0][search][value]': '',
            'columns[0][search][regex]': 'false',
            'columns[1][data]': '1',
            'columns[1][name]': '',
            'columns[1][searchable]': 'true',
            'columns[1][orderable]': 'false',
            'columns[1][search][value]': '',
            'columns[1][search][regex]': 'false',
            'columns[2][data]': '2',
            'columns[2][name]': '',
            'columns[2][searchable]': 'true',
            'columns[2][orderable]': 'true',
            'columns[2][search][value]': '',
            'columns[2][search][regex]': 'false',
            'columns[3][data]': '3',
            'columns[3][name]': '',
            'columns[3][searchable]': 'true',
            'columns[3][orderable]': 'true',
            'columns[3][search][value]': '',
            'columns[3][search][regex]': 'false',
            'columns[4][data]': '4',
            'columns[4][name]': '',
            'columns[4][searchable]': 'true',
            'columns[4][orderable]': 'true',
            'columns[4][search][value]': '',
            'columns[4][search][regex]': 'false',
            'columns[5][data]': '5',
            'columns[5][name]': '',
            'columns[5][searchable]': 'true',
            'columns[5][orderable]': 'true',
            'columns[5][search][value]': '',
            'columns[5][search][regex]': 'false',
            'columns[6][data]': '6',
            'columns[6][name]': '',
            'columns[6][searchable]': 'true',
            'columns[6][orderable]': 'true',
            'columns[6][search][value]': '',
            'columns[6][search][regex]': 'false',
            'columns[7][data]': '7',
            'columns[7][name]': '',
            'columns[7][searchable]': 'true',
            'columns[7][orderable]': 'true',
            'columns[7][search][value]': '',
            'columns[7][search][regex]': 'false',
            'columns[8][data]': '8',
            'columns[8][name]': '',
            'columns[8][searchable]': 'true',
            'columns[8][orderable]': 'true',
            'columns[8][search][value]': '',
            'columns[8][search][regex]': 'false',
            'columns[9][data]': '9',
            'columns[9][name]': '',
            'columns[9][searchable]': 'true',
            'columns[9][orderable]': 'true',
            'columns[9][search][value]': '',
            'columns[9][search][regex]': 'false',
            'columns[10][data]': '10',
            'columns[10][name]': '',
            'columns[10][searchable]': 'true',
            'columns[10][orderable]': 'true',
            'columns[10][search][value]': '',
            'columns[10][search][regex]': 'false',
            'columns[11][data]': '11',
            'columns[11][name]': '',
            'columns[11][searchable]': 'true',
            'columns[11][orderable]': 'true',
            'columns[11][search][value]': '',
            'columns[11][search][regex]': 'false',
            'columns[12][data]': '12',
            'columns[12][name]': '',
            'columns[12][searchable]': 'true',
            'columns[12][orderable]': 'true',
            'columns[12][search][value]': '',
            'columns[12][search][regex]': 'false',
            'columns[13][data]': '13',
            'columns[13][name]': '',
            'columns[13][searchable]': 'true',
            'columns[13][orderable]': 'true',
            'columns[13][search][value]': '',
            'columns[13][search][regex]': 'false',
            'columns[14][data]': '14',
            'columns[14][name]': '',
            'columns[14][searchable]': 'true',
            'columns[14][orderable]': 'false',
            'columns[14][search][value]': '',
            'columns[14][search][regex]': 'false',
            'columns[15][data]': '15',
            'columns[15][name]': '',
            'columns[15][searchable]': 'true',
            'columns[15][orderable]': 'false',
            'columns[15][search][value]': '',
            'columns[15][search][regex]': 'false',
            'start': '0',
            'length': '100',
            'search[value]': '',
            'search[regex]': 'false',
            'filter[YEAR]': f'lot_year:"{self.from_yers}"',
            'filter[FETI]': 'buy_it_now_code:B1',
            'query': f'{self.car}',
            'watchListOnly': 'false',
            'freeFormSearch': 'true',
            'page': '0',
            'size': '200',
            'includeTagByField[YEAR]': '{!tag=YEAR}'
        }

        response = requests.post('https://www.copart.com/public/lots/search', headers=headers, cookies=cookies,
                                 data=data)
        data = response.json()

        # Массив машин
        info_car = []

        for i in range(1000):
            try:
                name = data['data']['results']['content'][i]['ld']
                image = data['data']['results']['content'][i]['tims']
                price = data['data']['results']['content'][i]['hb']
                link_about = data['data']['results']['content'][i]['ldu']
                carNumber = data['data']['results']['content'][i]['lotNumberStr']
                url = f'https://www.copart.com/lot/{carNumber}/{link_about}'
                info_car.append([name, price, image, url])
            except:
                break
        # TODO: Придумать как и куда записывать данные в .json
        return info_car


class Copart:

    def __init__(self, id_user, car_name, from_year):
        self.id = id_user
        self.car = car_name
        self.from_yers = from_year

    def write_info_car_copart(self):
        copartcarinfo = CopartCarInfo(self.car, self.from_yers)
        data = copartcarinfo.get_car()

        for dt in data:
            try:
                with open(f'{self.id}.txt', 'a') as file:
                    file.write(f'{dt[0]}:{dt[1]}:{dt[2]}:{dt[3]}' + '\n')
            except:
                with open(f'{self.id}.txt', 'w') as file:
                    file.write(f'{dt[0]}:{dt[1]}:{dt[2]}:{dt[3]}' + '\n')

            file.close()
        logger.debug('Car Accepted')
