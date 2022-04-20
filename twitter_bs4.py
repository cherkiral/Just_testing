import requests
from bs4 import BeautifulSoup
import json
from pprint import pprint

user_id1 = '1199076320686284800'
auth_token = 'e6feb3581da4d28bbc77794ea0e1ec8a433b351b'
csrf_token = '89ef1a2b814d8840a5f3556c961e91e4aa5163ca8baa395b8847c55e00febab4ab8e4aa63b0cf860036fccd0dee14c961a29d086bd5947cce989d7fde50a2efae35db565defa6058027ad80d8d3a89b8'
authorization_bearer = 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA'


proxies = {
    'https': 'http://t6CauBkh:AhDnyuC3@62.76.7.247:50782'
}

def blockAccount(user_id, auth_token, csrf_token, authorization_bearer):
    url_block = "https://twitter.com/i/api/1.1/blocks/create.json"
    data = "user_id=%s" % user_id
    cookie = "ct0=%s; auth_token=%s" % (csrf_token, auth_token)
    user_agent = { 'User-Agent' : 'Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0', 'X-Csrf-Token' : csrf_token, 'Content-Type' : 'application/x-www-form-urlencoded', 'Authorization' :  authorization_bearer, 'Cookie' : cookie  }
    r = requests.post(url_block, verify=False, headers=user_agent, data=data, proxies=proxies)
    r_id = json.loads(r.text)['id_str']
    if (r_id == user_id):
        print("[+] User blocked: %s" % r_id)


def post_tweet(auth_token, csrf_token, authorization_bearer):
    url_block = "https://api.twitter.com/1.1/statuses/update.json"
    data = {"status":"Today i a great day"}
    cookie = "ct0=%s; auth_token=%s" % (csrf_token, auth_token)
    user_agent = { 'User-Agent' : 'Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0', 'X-Csrf-Token' : csrf_token, 'Content-Type' : 'application/x-www-form-urlencoded', 'Authorization' :  authorization_bearer, 'Cookie' : cookie  }
    r = requests.post(url_block, verify=False, headers=user_agent, data=data, proxies=proxies)
    print(r.text)

post_tweet(auth_token, csrf_token, authorization_bearer)

