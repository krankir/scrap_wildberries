import fake_useragent
import requests
import csv


class ScrapWB:
    def __init__(self, url: str):
        self.url = url

    def parse(self):
        user = fake_useragent.UserAgent().random

        headers = {
            'Sec-Fetch-Site': 'cross-site',
            'Accept': '*/*',
            'Origin': 'https://www.wildberries.ru',
            'Sec-Fetch-Dest': 'empty',
            'Accept-Language': 'ru',
            'Sec-Fetch-Mode': 'cors',
            'Host': 'catalog.wb.ru',
            'User-Agent': user,
            'Referer': 'https://www.wildberries.ru/',
            'Connection': 'keep-alive',
        }
        while True:
            response = requests.get(
                'https://catalog.wb.ru/brands/g/catalog?&appType=1&brand=28928&curr=rub&dest=-1579610&regions=80,38,4,64,83,33,68,70,69,30,86,40,1,66,110,22,31,48,114&sort=popular&spp=26',
                headers=headers,
            )


    def __create_csv(self):
        with open('wb_data.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['id',
                             'название',
                             'цена',
                             'бренд',
                             'продаж',
                             'рейтинг',
                             'в наличии']
                            )

    def __save_csv(self):
        ...


if __name__ == '__main__':
    ScrapWB('https://www.wildberries.ru/brands/gigabyte').parse()
