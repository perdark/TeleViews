import random
import urllib
import requests
from threading import Thread
link1 = "https://t.me/B_2_V/172"
views = 0
https = requests.get("https://api.proxyscrape.com/?request=displayproxies&proxytype=https&timeout=0",
                     proxies=urllib.request.getproxies(), ).text
http = requests.get("https://api.proxyscrape.com/?request=displayproxies&proxytype=http&timeout=0",
                    proxies=urllib.request.getproxies(), ).text
prox_list = (https+http).split()


def send_seen(channel, msgid, proxy):
    s = requests.Session()
    proxies = {'http': proxy, 'https': proxy}
    try:
        a = s.get("https://t.me/"+channel+"/"+msgid,
                  timeout=10, proxies=proxies)
        cookie = a.headers['set-cookie'].split(';')[0]
    except Exception as e:
        return
    h1 = {"Accept": "*/*", "Accept-Encoding": "gzip, deflate, br", "Accept-Language": "en-US,en;q=0.9,fa;q=0.8,de;q=0.7", "Connection": "keep-alive", "Content-Length": "5", "Content-type": "application/x-www-form-urlencoded",
          "Cookie": cookie, "Host": "t.me", "Origin": "https://t.me", "Referer": "https://t.me/"+channel+"/"+msgid+"?embed=1", "Sec-Fetch-Dest": "empty", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Site": "same-origin", "User-Agent": "Chrome"}
    d1 = {"_rl": "1"}
    try:
        r = s.post('https://t.me/'+channel+'/'+msgid+'?embed=1',
                   json=d1, headers=h1, proxies=proxies)
        key = r.text.split('data-view="')[1].split('"')[0]
        now_view = r.text.split('<span class="tgme_widget_message_views">')[
            1].split('</span>')[0]
        if now_view.find("K") != -1:
            now_view = now_view.replace("K", "00").replace(".", "")
    except Exception as e:
        return
    h2 = {"Accept": "*/*", "Accept-Encoding": "gzip, deflate, br", "Accept-Language": "en-US,en;q=0.9,fa;q=0.8,de;q=0.7", "Connection": "keep-alive", "Cookie": cookie, "Host": "t.me",
          "Referer": "https://t.me/"+channel+"/"+msgid+"?embed=1", "Sec-Fetch-Dest": "empty", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Site": "same-origin", "User-Agent": "Chrome", "X-Requested-With": "XMLHttpRequest"}
    try:
        i = s.get('https://t.me/v/?views='+key, timeout=10,
                  headers=h2, proxies=proxies)
        if(i.text == "true"):
            print('Views :'+now_view)
            views += 1
    except Exception as e:
        return
    try:
        h3 = {"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9", "Accept-Encoding": "gzip, deflate, br", "Accept-Language": "en-US,en;q=0.9,fa;q=0.8,de;q=0.7",
              "Cache-Control": "max-age=0", "Connection": "keep-alive", "Cookie": cookie, "Host": "t.me", "Sec-Fetch-Dest": "document", "Sec-Fetch-Mode": "navigate", "Sec-Fetch-Site": "none", "Sec-Fetch-User": "?1", "Upgrade-Insecure-Requests": "1", "User-Agent": "Chrome"}
        s.get("https://t.me/"+channel+"/"+msgid, headers=h3,
              timeout=10, proxies=proxies)
    except Exception as e:
        return


while True:
    try :
        th = Thread(target=send_seen, args=(
            "B_2_V", "172", random.choice(prox_list)))
        th.start()
    except:
        pass
