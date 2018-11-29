#! python3

import requests
import re

url = 'https://page.com/form'



def fetch():
  with requests.Session() as s:
    get = s.get(url)
    set_cookie = get.headers['Set-Cookie']
    print('set_cookie, type:\t', set_cookie)
    csrftoken = re.compile('csrftoken=([^;]*);').search(set_cookie).group(1)
    print('csrftoken:\t', csrftoken)
    data = {
      "csrfmiddlewaretoken": csrftoken,
      "name": "Ola Nordmann",
      "email": "olan@epost.no",
      "contact_plus_form_3674": "Send",
      "from": "web"
    }
    post = s.post(url, data=data)
    print('post:\t', post)
    print('post.text:\n', post.text)



fetch()
