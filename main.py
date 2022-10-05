import requests, re, threading,urllib,random
from colorama import Fore

link = input(' [#] رابط المنشور ').replace('https://', '').replace('http://', '')
_threads = int(input(' [#] عدد المشاهدات '))
https = requests.get("https://api.proxyscrape.com/?request=displayproxies&proxytype=https&timeout=0",
                     proxies=urllib.request.getproxies(), ).text
http = requests.get("https://api.proxyscrape.com/?request=displayproxies&proxytype=http&timeout=0",
                    proxies=urllib.request.getproxies(), ).text
main_url = f'https://{link}?embed=1'
views_url = 'https://t.me/v/?views='
#proxies = (https).split()
proxies = ['45.63.100.155:10119\n', '154.236.179.226:1981\n', '201.150.116.81:999\n', '89.38.96.219:3128\n', '110.78.138.65:8080\n', '41.65.55.10:1981\n', '189.173.168.174:999\n', '152.231.29.51:8080\n', '165.16.5.166:9999\n', '161.82.183.156:80\n', '149.28.13.113:10691\n', '142.154.69.76:8080\n', '41.65.251.85:1976\n', '51.159.207.156:3128\n', '194.5.193.73:8080\n', '45.70.236.123:999\n', '62.193.108.138:1976\n', '149.28.13.113:10691\n', '93.180.135.243:3128\n', '79.142.95.90:55443\n', '41.65.251.85:1976\n', '201.71.2.120:999\n', '70.90.138.109:8080\n', '71.19.240.35:3128\n', '161.82.183.156:80\n', '103.164.151.51:3125\n', '146.19.191.116:3128\n', '115.147.10.1:8080\n', '46.23.148.204:8080\n', '91.122.220.100:8080\n', '139.84.162.173:3128\n', '93.180.135.243:3128\n', '202.137.3.209:3888\n', '201.204.50.188:999\n', '118.137.70.48:8080\n', '54.36.246.74:8080\n', '96.95.164.41:3128\n', '45.76.9.121:10731\n', '24.109.252.48:80\n', '41.65.236.57:1981\n', '41.65.55.2:1976\n', '192.166.230.113:3128\n', '204.48.29.183:13420\n', '145.40.121.169:3128\n', '173.212.200.30:3128\n', '196.219.202.74:8080\n', '142.147.114.50:8080\n', '110.78.138.65:8080\n', '201.71.2.120:999\n', '37.210.74.196:8080\n', '62.193.108.144:1981\n', '115.147.10.1:8080\n', '187.200.52.188:999\n', '188.242.219.58:8080\n', '157.100.53.99:999\n', '185.125.125.157:80\n', '192.99.54.97:13917\n', '190.108.82.109:999\n', '95.79.25.77:3128\n', '41.65.236.57:1981\n', '192.99.54.97:14044\n', '41.65.55.10:1976\n', '103.168.129.123:8080\n', '181.129.49.214:999\n', '217.70.28.188:8080\n', '195.14.22.173:80\n', '61.7.184.124:8080\n', '103.75.118.111:4443\n', '41.33.99.18:8080\n', '45.173.231.155:999\n', '45.224.149.246:999\n', '45.71.113.97:999\n', '46.29.76.71:8080\n', '192.166.230.113:3128\n', '45.233.67.226:999\n', '182.52.51.10:61124\n', '103.137.218.105:83\n', '139.255.88.52:3128\n', '41.216.186.128:3128\n', '103.163.231.189:8080\n', '110.172.151.146:8080\n', '191.252.195.53:8888\n', '191.102.250.6:8085\n', '45.63.100.155:10119\n', '191.97.9.130:999\n', '195.250.92.58:8080\n', '154.236.168.179:1976\n', '185.134.49.179:3128\n', '177.52.221.47:999\n', '116.203.124.57:3128\n', '192.99.54.97:13780\n', '217.70.28.188:8080\n', '185.134.49.179:3128\n', '222.253.48.253:8080\n', '187.200.52.188:999\n', '110.172.151.146:8080\n', '20.54.56.26:8080\n', '104.238.220.251:3128\n', '103.180.119.17:9090\n', '89.38.96.219:3128\n', '203.84.136.139:8088\n', '41.65.236.57:1981\n', '128.199.67.35:80\n', '185.125.125.157:80\n', '179.49.117.226:999\n', '23.106.47.15:3128\n', '181.225.73.34:8080\n', '181.36.121.236:999\n', '190.217.101.73:999\n', '38.41.0.94:999']
#with open("v.txt","r") as f :
#	proxies = f.readlines()
sent, bad_proxy, done, next_proxy = 0, 0, 0, 0

_headers = {
  'accept-language': 'en-US,en;q=0.9',
  'user-agent': 'Mozilla/5.0 (Linux; Android 10; SM-G981B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Mobile Safari/537.36',
  'x-requested-with': 'XMLHttpRequest'
}


def send_views():
    global sent, bad_proxy, done, next_proxy
    while True:
        proxy = random.choice(proxies)
        try:
            session = requests.session()
            session.proxies.update({'http': f'http://{proxy}', 'https': f'http://{proxy}'})
            session.headers.update(_headers)
            main_res = session.get(main_url).text
            _token = re.search('data-view="([^"]+)', main_res).group(1)
            views_req = session.get(views_url + _token)
            print(Fore.GREEN+' [+] View Sent ' + 'Stats Code: '+str(views_req.status_code)+Fore.RESET)
            with open("v.txt","a") as f :
            	f.write(f"\n{proxy}")
            sent += 1
            done += 1
        except requests.exceptions.ConnectionError:
            try :
            	proxies.remove(proxy)
            except :
            	pass
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
