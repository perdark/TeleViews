import requests, re, threading,urllib
from colorama import Fore

link = input(' [#] رابط المنشور ').replace('https://', '').replace('http://', '')
_threads = int(input(' [#] عدد المشاهدات '))
https = requests.get("https://api.proxyscrape.com/?request=displayproxies&proxytype=https&timeout=0",
                     proxies=urllib.request.getproxies(), ).text
http = requests.get("https://api.proxyscrape.com/?request=displayproxies&proxytype=http&timeout=0",
                    proxies=urllib.request.getproxies(), ).text
main_url = f'https://{link}?embed=1'
views_url = 'https://t.me/v/?views='
proxies = (http+https).split()

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
            print(Fore.GREEN+' [+] View Sent ' + 'Stats Code: '+str(views_req.status_code)+Fore.RESET)
            sent += 1
            done += 1
        except requests.exceptions.ConnectionError:
            proxies.remove(proxy)
            print(Fore.RED+' [x] Bad Proxy: ' + proxy+Fore.RESET)
            bad_proxy += 1
            done += 1
Threads = []
for t in range(_threads):
    x = threading.Thread(target=send_views)
    x.start()
    Threads.append(x)

for Th in Threads:
    Th.join()
