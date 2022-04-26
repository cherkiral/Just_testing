import json
import time
import sys
import requests
import urllib3
import inspect

start_time = time.time()
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def post_tweet(aurhorization_list, message):
    url_block = "https://api.twitter.com/1.1/statuses/update.json"
    data = {"status": message}
    cookie = "ct0=%s; auth_token=%s" % (aurhorization_list['csrf_token'], aurhorization_list['auth_token'])
    user_agent = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0',
                  'X-Csrf-Token': aurhorization_list['csrf_token'], 'Content-Type': 'application/x-www-form-urlencoded',
                  'Authorization': aurhorization_list['authorization_bearer'], 'Cookie': cookie}
    r = requests.post(url_block, verify=False, headers=user_agent, data=data, proxies=aurhorization_list['proxies'])

    try:
        status = json.loads(r.text)['text']
        if status == message:
            print('Успешно твитнуто')
        else:
            print(r.text)
    except Exception:
        print(f'ОШИБКА В ФУНКЦИИ: {inspect.getframeinfo(inspect.currentframe()).function}')
        print(r.text)

def like_post(aurhorization_list, tweet_id):
    url_block = "https://api.twitter.com/1.1/favorites/create.json"
    data = {"id": tweet_id}
    cookie = "ct0=%s; auth_token=%s" % (aurhorization_list['csrf_token'], aurhorization_list['auth_token'])
    user_agent = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0',
                  'X-Csrf-Token': aurhorization_list['csrf_token'], 'Content-Type': 'application/x-www-form-urlencoded',
                  'Authorization': aurhorization_list['authorization_bearer'], 'Cookie': cookie}
    r = requests.post(url_block, verify=False, headers=user_agent, data=data, proxies=aurhorization_list['proxies'])

    try:
        status = r.json()['favorited']
        if status == True:
            print('Успешно лайкнул твит')
        else:
            print(r.text)
    except Exception as err:
        print(f'ОШИБКА В ФУНКЦИИ: {inspect.getframeinfo(inspect.currentframe()).function}')
        try:
            status = json.loads(r.text)['errors'][0]['message']
            if status == 'You have already favorited this status.':
                print('Твит уже лайкнут')
            else:
                print(r.text)
        except Exception as err:
            print(f'ОШИБКА В ФУНКЦИИ: {inspect.getframeinfo(inspect.currentframe()).function}')
            print(r.text)



def retweet_post(aurhorization_list, tweet_id):
    url_block = f"https://api.twitter.com/1.1/statuses/retweet/{tweet_id}.json"
    data = {"id": tweet_id}
    cookie = "ct0=%s; auth_token=%s" % (aurhorization_list['csrf_token'], aurhorization_list['auth_token'])
    user_agent = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0',
                  'X-Csrf-Token': aurhorization_list['csrf_token'], 'Content-Type': 'application/x-www-form-urlencoded',
                  'Authorization': aurhorization_list['authorization_bearer'], 'Cookie': cookie}
    r = requests.post(url_block, verify=False, headers=user_agent, data=data, proxies=aurhorization_list['proxies'])

    try:
        status = r.json()["retweeted"]
        if status == True:
            print('Успешно ретвитнул')
        else:
            print(r.text)
    except Exception as err:
        print(f'ОШИБКА В ФУНКЦИИ: {inspect.getframeinfo(inspect.currentframe()).function}')
        try:
            status = json.loads(r.text)['errors'][0]['message']
            if status == "You have already retweeted this Tweet.":
                print('Пост уже ретвитнут')
            else:
                print(r.text)
        except Exception as err:
            print(f'ОШИБКА В ФУНКЦИИ: {inspect.getframeinfo(inspect.currentframe()).function}')
            print(r.text)

def follow_user(aurhorization_list, user_id):
    url_block = "https://api.twitter.com/1.1/friendships/create.json"
    data = {"user_id": user_id}
    cookie = "ct0=%s; auth_token=%s" % (aurhorization_list['csrf_token'], aurhorization_list['auth_token'])
    user_agent = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0',
                  'X-Csrf-Token': aurhorization_list['csrf_token'], 'Content-Type': 'application/x-www-form-urlencoded',
                  'Authorization': aurhorization_list['authorization_bearer'], 'Cookie': cookie}
    r = requests.post(url_block, verify=False, headers=user_agent, data=data, proxies=aurhorization_list['proxies'])

    try:
        status = json.loads(r.text)['following']
        if status == True:
            print('Успешно подписан')
        else:
            print(r.text)
    except Exception as err:
        print(f'ОШИБКА В ФУНКЦИИ {inspect.getframeinfo(inspect.currentframe()).function}: ')
        print(r.text)


def check_follow():
    pass

def comment_tweet(aurhorization_list, message, tweet_id): #пример: https://twitter.com/JamesMelville/status/1516669369677406208
    url_block = "https://api.twitter.com/1.1/statuses/update.json"
    data = {"status": message, 'in_reply_to_status_id': tweet_id, 'auto_populate_reply_metadata': True}
    cookie = "ct0=%s; auth_token=%s" % (aurhorization_list['csrf_token'], aurhorization_list['auth_token'])
    user_agent = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0',
                  'X-Csrf-Token': aurhorization_list['csrf_token'], 'Content-Type': 'application/x-www-form-urlencoded',
                  'Authorization': aurhorization_list['authorization_bearer'], 'Cookie': cookie}
    r = requests.post(url_block, verify=False, headers=user_agent, data=data, proxies=aurhorization_list['proxies'])

    try:
        status = json.loads(r.text)['text']
        if message.split()[0] in status:
            print('Успешно оставлен комментарий')
        else:
            print(r.text)
    except Exception as err:
        print(f'ОШИБКА В ФУНКЦИИ: {inspect.getframeinfo(inspect.currentframe()).function}')
        try:
            status = json.loads(r.text)['errors'][0]['message']
            if status == "Status is a duplicate.":
                print('Комментарий уже оставлен')
            else:
                print(r.text)
        except Exception as err:
            print(f'ОШИБКА В ФУНКЦИИ: {inspect.getframeinfo(inspect.currentframe()).function}')
            print(r.text)


def quote_tweet_post(aurhorization_list, message, tweet_status): #пример: https://twitter.com/JamesMelville/status/1516669369677406208
    url_block = "https://api.twitter.com/1.1/statuses/update.json"
    data = {"status": message, 'attachment_url': tweet_status}
    cookie = "ct0=%s; auth_token=%s" % (aurhorization_list['csrf_token'], aurhorization_list['auth_token'])
    user_agent = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0',
                  'X-Csrf-Token': aurhorization_list['csrf_token'], 'Content-Type': 'application/x-www-form-urlencoded',
                  'Authorization': aurhorization_list['authorization_bearer'], 'Cookie': cookie}
    r = requests.post(url_block, verify=False, headers=user_agent, data=data, proxies=aurhorization_list['proxies'])


    if r.status_code < 500:
        try:
            status = json.loads(r.text)['text']
            if status == message:
                print('Успешно quote tweet')
        except Exception as err:
            print(f'ОШИБКА В ФУНКЦИИ: {inspect.getframeinfo(inspect.currentframe()).function}')

            pass

        try:
            status = json.loads(r.text)['errors'][0]['message']
            if status == "Status is a duplicate.":
                print('Quote tweet уже сделан')
        except Exception as err:
            print(f'ОШИБКА В ФУНКЦИИ: {inspect.getframeinfo(inspect.currentframe()).function}')

            pass
    else:
        print(r.text)