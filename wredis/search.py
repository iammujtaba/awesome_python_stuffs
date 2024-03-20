import eventlet
# note: this urllib import doesn't work in Python2
from eventlet.green.urllib.request import urlopen


urls = [
    "http://www.google.com/intl/en_ALL/images/logo.gif",
    "https://i.wlycdn.com/wealthy-home-page/wealthy-landing-page-our-moto.png",
    # "https://i.wlycdn.com/wealthy-home-page/partner-page-hero-image-aditya.png",
    "http://www.google.com/intl/en_ALL/images/logo.gif",
]


def fetch(url):
    return urlopen(url).read()


pool = eventlet.GreenPool()

import time

res = pool.imap(fetch, urls)
for body in pool.imap(fetch, urls):
    print("got body", len(body))




import gevent
from gevent import socket
urls = ['https://www.google.com', 'https://www.wealthy.in', 'https://www.python.org']
# urls = [
#     "http://www.google.com/intl/en_ALL/images/logo.gif",
#     "https://i.wlycdn.com/wealthy-home-page/wealthy-landing-page-our-moto.png",
#     # "https://i.wlycdn.com/wealthy-home-page/partner-page-hero-image-aditya.png",
#     "http://www.google.com/intl/en_ALL/images/logo.gif",
# ]
import requests
import time

start = time.time()
jobs = [gevent.spawn(requests.get, url) for url in urls]
_ = gevent.joinall(jobs, timeout=1)
[job.value for job in jobs]
print(time.time() - start)

start = time.time()
for url in urls:
    print(requests.get(url).status_code)
print(time.time() - start)
