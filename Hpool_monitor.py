import requests
from rich import print
from sys import platform


class Hpool:
    def __init__(self):
        self.URL = 'https://www.hpool.com/api/pool/detail?language=zh&type=chia'
        self.HEADERS = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0',
            'Cookie': '!! YOUR LOGIN COOKIES !!',
        }

    def hpool_monitor(self):
        response = requests.get(url=self.URL, headers=self.HEADERS)
        response.encoding = 'utf-8'
        response = response.json()
        if response['code'] == 202 and response['message'] == 'Not login':
            print('[bold red]' + response['message'] + '[/bold red]')
            exit(0)
        if response['code'] == 200:
            response = response['data']

            print('API Key : ' + response['api_key'])
            print('[bold green]Online : ' + str(response['online']) + '[/bold green] | [bold red]Offline : ' + str(response['offline']) + '[/bold red]')
            print('有效算力 : [bold green]' + str(round(int(response['capacity']) / 1024, 2)) + ' TiB[/bold green]')
            print('Pool Address : ' + response['pool_address'])

    def run(self):
        self.hpool_monitor()


if __name__ == '__main__':
    try:
        assert ('win' in platform), 'only windows platform'.title()
        from os import system
        Hpool().run()
        system('pause')
    except AssertionError as AE:
        print(AE)
