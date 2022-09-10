import requests

import requests, re, threading

link = input(' [#] رابط المنشور ').replace('https://', '').replace('http://', '')
_threads = int(input(' [#] عدد المشاهدات '))

main_url = f'https://{link}?embed=1'
views_url = 'https://t.me/v/?views='

proxies = requests.get("https://apis.clouduz.ru/api/virus.php?type=all").text.splitlines()
count_proxies = len(proxies)

sent, bad_proxy, done, next_proxy = 0, 0, 0, 0

_headers = {
  'accept-language': 'en-US,en;q=0.9',
  'user-agent': 'Mozilla/5.0 (Linux; Android 10; SM-G981B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Mobile Safari/537.36',
  'x-requested-with': 'XMLHttpRequest'
}


def send_views():
    global sent, bad_proxy, done, next_proxy
    while True:
        try:
            proxy = proxies[next_proxy]
            next_proxy += 1
        except IndexError:
            break
        try:
            session = requests.session()
            session.proxies.update({'http': f'http://{proxy}', 'https': f'http://{proxy}'})
            session.headers.update(_headers)
            main_res = session.get(main_url).text
            _token = re.search('data-view="([^"]+)', main_res).group(1)
            views_req = session.get(views_url + _token)
            print(' [+] View Sent ' + 'Stats Code: '+str(views_req.status_code))
            sent += 1
            done += 1

        except requests.exceptions.ConnectionError:
            print(' [x] Bad Proxy: ' + proxy)
            bad_proxy += 1
            done += 1


Threads = []
for t in range(_threads):
    x = threading.Thread(target=send_views)
    x.start()
    Threads.append(x)

for Th in Threads:
    Th.join()
