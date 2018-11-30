#! python3

import re
import requests
from threading import Thread, active_count

url = 'https://page.com/form'
number_of_requests = 100

def fetch():
  with requests.Session() as s:
    get = s.get(url)
    print('get', get)
    set_cookie = get.headers['Set-Cookie']
    csrftoken = re.compile('csrftoken=([^;]*);').search(set_cookie).group(1)
    data = {
      "csrfmiddlewaretoken": csrftoken,
      "name": "Ola Nordmann",
      "email": "olan@epost.no",
      "contact_plus_form_3674": "Send",
      "from": "web"
    }
    post = s.post(url, data=data)
    print('post', post)


def setup_threads(n_threads):
    return [Thread(target=fetch) for _ in range(n_threads)]


# Setup and start, and wait for threads
threads = setup_threads(number_of_requests)
[thread.start() for thread in threads]
[thread.join(2.5) for thread in threads]

print("All threads finished")
