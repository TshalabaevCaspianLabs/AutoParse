from multiprocessing import Pool

import requests
from bs4 import BeautifulSoup as bs
from loguru import logger


class Links:

    def __init__(self, car_name, from_year):
        self.car = car_name
        self.from_year = from_year

    def get_html(self):
        cookies = {
            '_fbp': 'fb.1.1618075380524.277207766',
            'kampyleSessionPageCounter': '2',
            'kampyleUserPercentile': '79.1027485746737',
            '_ga': 'GA1.2.1714835462.1618075395',
            '_gid': 'GA1.2.1175105592.1618569715',
            '_uetsid': '5d0489609ea011eb87fc9df2bee738d8',
            '_uetvid': '6618ff609a2111eb839a8ffe6cf76fae',
            'OptanonAlertBoxClosed': '2021-04-16T11:07:51.535Z',
            'OptanonConsent': 'isIABGlobal=false&datestamp=Fri+Apr+16+2021+16%3A07%3A51+GMT%2B0500+(%2B05)&version=6.1.0&consentId=13d2070a-f39c-4672-b673-491ad1b4348b&interactionCount=0&landingPath=NotLandingPage&groups=C0001%3A1%2CC0003%3A1%2CC0002%3A1%2CC0004%3A1&hosts=&legInt=&AwaitingReconsent=false&geolocation=%3B',
            'IAAITrackingCookie': 'a0ea3a23-9e8e-4517-ac4b-cc9016530bc3',
            'URICookie': 'URI=mYYQY3U4qknza%2bL3Jf5x2SnAM3ukK1xqGxOrg0Hf2cM%3d',
            'cto_bundle': '0BdGWV9teCUyQnVkS29jT0pvUzE5bnglMkZidmNTQmtlTGlBMTREcWx6JTJCOW9ieHNQTUFRT01Ja0ZzZmlWTE9sMDFmbzBCQTBMa1dzYUZzTU1SY1JrTDNwYlNabWZvVEliMkNheGZEWFhQRmNBZVZmWHJyV2RidlRpWjJVdnBkSHhvQ3AlMkZNWVFmanVWZjg1OTRiZ1pYSFlVeEk0SDluREYlMkJwWEp5RHljenVCOEcyVlNDaFM0JTNE',
            'kampyleUserSession': '1618570909670',
            'kampyleUserSessionsCount': '10',
            'cto_bidid': 'mja0Kl9TdmIlMkYwd0V3SjNpb0NYcXN6TURkYkZTMVEwT251WkU3eXJvTkNoOEVvJTJGdDQ2TmZFNmRrV2diYzFGVUdsWjVsTDhzTER0dkdtRVIzUHhkM3ZhdVRKUlFmOUZ0dUlzSCUyQlNYT0I5NXZmZUVhWSUzRA',
            'cto_test_cookie': '',
            'optimizelyEndUserId': 'oeu1618075395050r0.9775158124867507',
            '__gads': 'ID=f95b0a6c2b252089-22abb6bd22bb009a:T=1618570829:RT=1618570829:S=ALNI_MbH1h0JYScFgldc45w1UTnDWE_xtw',
            '__mguid_': 'aeb9bf17-d721-4b3c-b9e4-6b022f544577',
            'PreviousSortSalesList': 'saleslist?url=d+W1cSsHGtpuDZLQpJZyEYAEZ3pbGDVdy1W9hbs5PDezF01bqCp8LZFirxYosqja',
            'DECLINED_DATE': '1618179777850',
            'LAST_INVITATION_VIEW': '1618179774806',
            'BIGipServerl_www.iaai.com_80_pool': 'rd20o00000000000000000000ffffac11f09co80',
            'ASLBSA': 'eaa30060551c6c375b9c300c315d81f75dfb5f868570ab9fa5b832a43ef4276f',
            'ASLBSACORS': 'eaa30060551c6c375b9c300c315d81f75dfb5f868570ab9fa5b832a43ef4276f',
            'ASP.NET_SessionId': 'wi2vsb42sp1g12aoxi3crqhv',
            'SearchIntroCookie': 'true',
            'cd_user_id': '178bcceefb3893-0669a0a4aa228a8-48183301-13c680-178bcceefb4b57',
            'kampyle_userid': '19e5-8978-fc3d-5c95-16ac-3a8c-06f4-d172',
            'Locations_Cookie': 'Locations_Cookie=MapView',
        }
        headers = {
            'Content-Type': 'application/json',
            'Pragma': 'no-cache',
            'Accept': '*/*',
            'Accept-Language': 'ru',
            'Accept-Encoding': 'gzip, deflate, br',
            'Cache-Control': 'no-cache',
            'Host': 'www.iaai.com',
            'Origin': 'https://www.iaai.com',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Safari/605.1.15',
            'Referer': 'https://www.iaai.com/Search?url=mYYQY3U4qknza%2bL3Jf5x2SnAM3ukK1xqGxOrg0Hf2cM%3d',
            'Content-Length': '195',
            'Connection': 'keep-alive',
        }
        params = (
            ('c', '1618571375685'),
        )

        data = '{"Searches":[{"Facets":null,"FullSearch":"%s","LongRanges":null},{"Facets":[{"Group":"QuickLinkCategories","Value":"I-Buy Fast"}],"FullSearch":null,"LongRanges":null},{"Facets":null,"FullSearch":"%s","LongRanges":null},{"Facets":null,"FullSearch":null,"LongRanges":[{"From":%s,"Name":"Year","To":2022}]}],"miles":0,"PageSize":100,"CurrentPage":1}' % (
            self.car, self.car, self.from_year)

        response = requests.post('https://www.iaai.com/Search/GetSearchResults', headers=headers, params=params,
                                 cookies=cookies, data=data)
        # Получаем html код начальной страницы запроса
        return response.text

    def parse_html(self):
        html = self.get_html()
        soup = bs(html, 'lxml')
        h4_list = soup.find_all('h4', class_='heading-7 rtl-disabled')
        links = []
        for h4 in h4_list:
            link = h4.find('a').get('href')
            links.append('https://www.iaai.com' + link)
        # Получаем все ссылки со страницы с запросом на лоты
        return links


class Iaai:

    def __init__(self, id_user, car_name, from_year):
        self.id = id_user
        self.car = car_name
        self.from_year = from_year

    #  парсинг полученых ссылок (достаем Название машины, цену,
    def get_info_car(self, url):
        global price
        cookies = {
            'IAAITrackingCookie': 'a0ea3a23-9e8e-4517-ac4b-cc9016530bc3',
            'cto_bundle': 'T5aVrl9teCUyQnVkS29jT0pvUzE5bnglMkZidmNTSFR2b2xMZkVQcHJjQlVuVVRtaWJwblR6cWNJelBUb0xHWUdOd3MyM1cyYVUlMkZ6S2Nqa3RQdmRhTVglMkY0d3BJdEZwYzVTWWt4SW5EcGYlMkJBVmNPWmIlMkJEeXdpcnQlMkJvdiUyQmZseWYlMkZJZ09salBGaGklMkZieEpOJTJCbXl6WVlMJTJGNktPY0g5WnFwNW1PMUdjRUFGeG9ORDIlMkJrS0J4USUzRA',
            'kampyleSessionPageCounter': '1',
            'kampyleUserSession': '1618600975767',
            'kampyleUserSessionsCount': '13',
            'OB-USER-TOKEN': '82b6fc8e-30a1-4a4d-87ac-b183370e05de',
            '_fbp': 'fb.1.1618075380524.277207766',
            '_ga': 'GA1.2.1714835462.1618075395',
            '_gid': 'GA1.2.1175105592.1618569715',
            '_uetsid': '5d0489609ea011eb87fc9df2bee738d8',
            '_uetvid': '6618ff609a2111eb839a8ffe6cf76fae',
            'OptanonAlertBoxClosed': '2021-04-16T19:22:49.575Z',
            'OptanonConsent': 'isIABGlobal=false&datestamp=Sat+Apr+17+2021+00%3A22%3A49+GMT%2B0500+(%2B05)&version=6.1.0&consentId=13d2070a-f39c-4672-b673-491ad1b4348b&interactionCount=0&landingPath=NotLandingPage&groups=C0001%3A1%2CC0003%3A1%2CC0002%3A1%2CC0004%3A1&hosts=&legInt=&AwaitingReconsent=false&geolocation=%3B',
            'cto_bidid': 'lyJmKV9TdmIlMkYwd0V3SjNpb0NYcXN6TURkYkZTMVEwT251WkU3eXJvTkNoOEVvJTJGdDQ2TmZFNmRrV2diYzFGVUdsWjVsTGlpdlV0UjhQVVdNM1oyTiUyRkppaWU5UFRKejJ2N2x6S0lwZ2NqcEFGZlNnTSUzRA',
            'cto_test_cookie': '',
            'optimizelyEndUserId': 'oeu1618075395050r0.9775158124867507',
            '__gads': 'ID=f95b0a6c2b252089-22abb6bd22bb009a:T=1618570829:RT=1618600934:S=ALNI_MbH1h0JYScFgldc45w1UTnDWE_xtw',
            'URICookie': 'URI=oJttFICoz9JH%2bKNWPSzKJFscE%2fXfII2t5q93d6Vcpsk%3d&ZipCodeValue=',
            '__mguid_': 'aeb9bf17-d721-4b3c-b9e4-6b022f544577',
            'PreviousSortSalesList': 'saleslist?url=d+W1cSsHGtpuDZLQpJZyEYAEZ3pbGDVdy1W9hbs5PDezF01bqCp8LZFirxYosqja',
            'DECLINED_DATE': '1618179777850',
            'LAST_INVITATION_VIEW': '1618179774806',
            'BIGipServerl_www.iaai.com_80_pool': 'rd20o00000000000000000000ffffac11f09co80',
            'ASLBSA': 'eaa30060551c6c375b9c300c315d81f75dfb5f868570ab9fa5b832a43ef4276f',
            'ASLBSACORS': 'eaa30060551c6c375b9c300c315d81f75dfb5f868570ab9fa5b832a43ef4276f',
            'ASP.NET_SessionId': 'wi2vsb42sp1g12aoxi3crqhv',
            'SearchIntroCookie': 'true',
            'cd_user_id': '178bcceefb3893-0669a0a4aa228a8-48183301-13c680-178bcceefb4b57',
            'kampyle_userid': '19e5-8978-fc3d-5c95-16ac-3a8c-06f4-d172',
            'Locations_Cookie': 'Locations_Cookie=MapView',
        }
        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Host': 'www.iaai.com',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Safari/605.1.15',
            'Accept-Language': 'ru',
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive',
        }

        rowNumber = url.split('?tenant=US&RowNumber=')[1]  # номер лота на странице
        numberCar = url.split('https://www.iaai.com/vehicledetails/')[1].split('?')[0]  # id машины на сайте

        params = (('tenant', 'US'), ('RowNumber', f'{rowNumber}'),)
        response = requests.get(f'https://www.iaai.com/vehicledetails/{numberCar}', headers=headers, params=params,
                                cookies=cookies)
        html = response.text

        image_link = html.split('var testUrl = "')[1].split('";')[0]
        r = requests.get(image_link)
        image = r.text.split(',"keys":[{"K":"')[1].split('","')[0]

        params = (('imageKeys', f'{image}'), ('width', '200'), ('height', '200'),)
        response = requests.get('https://anvis.iaai.com/resizer', params=params)
        url_image = response.request.url

        soup = bs(html, 'lxml')
        name = soup.find('h1').text

        li_list = soup.find_all('li', class_='data-list__item')
        for li in li_list:
            try:
                span = li.find('span', class_='data-list__value').text.strip()
                if '$' in span:
                    price = span
                    break
            except Exception:
                pass

        try:
            with open(f'{self.id}.txt', 'a') as file:
                file.write(f'{name}:{price}:{url_image}:{url}'.strip() + '\n')
            file.close()
        except:
            with open(f'{self.id}.txt', 'w') as file:
                file.write(f'{name}:{price}:{url_image}:{url}'.strip() + '\n')
            file.close()
        logger.debug('Car Accepted')

    # Старт программы для сайта iaai
    def iaai(self):
        try:
            with Pool(40) as p:
                html = Links(self.car, self.from_year)
                links = html.parse_html()
                p.map(self.get_info_car, links)
        except Exception as e:
            pass
