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
    flag = 0

    if r.ok:
        try:
            status = json.loads(r.text)['text']
            if status == message:
                print('Успешно твитнуто')
        except Exception:
            flag += 1
            pass
    else:
        print(r.text)
    return flag

def like_post(aurhorization_list, tweet_id):
    url_block = "https://api.twitter.com/1.1/favorites/create.json"
    data = {"id": tweet_id}
    cookie = "ct0=%s; auth_token=%s" % (aurhorization_list['csrf_token'], aurhorization_list['auth_token'])
    user_agent = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0',
                  'X-Csrf-Token': aurhorization_list['csrf_token'], 'Content-Type': 'application/x-www-form-urlencoded',
                  'Authorization': aurhorization_list['authorization_bearer'], 'Cookie': cookie}
    r = requests.post(url_block, verify=False, headers=user_agent, data=data, proxies=aurhorization_list['proxies'])
    flag = 0

    if r.status_code < 500:
        try:
            status = json.loads(r.text)['errors'][0]['message']
            if status == 'You have already favorited this status.':
                print('Твит уже лайкнут')
        except Exception as err:
            print(f'ОШИБКА В ФУНКЦИИ: {err}')
            flag+=1
            pass

        try:
            status = r.json()['favorited']
            if status == True:
                print('Успешно лайкнул твит')
        except Exception as err:
            print(f'ОШИБКА В ФУНКЦИИ: {err}')
            flag += 1
            pass
    else:
        print(r.text)
    return flag

def retweet_post(aurhorization_list, tweet_id):
    url_block = f"https://api.twitter.com/1.1/statuses/retweet/{tweet_id}.json"
    data = {"id": tweet_id}
    cookie = "ct0=%s; auth_token=%s" % (aurhorization_list['csrf_token'], aurhorization_list['auth_token'])
    user_agent = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0',
                  'X-Csrf-Token': aurhorization_list['csrf_token'], 'Content-Type': 'application/x-www-form-urlencoded',
                  'Authorization': aurhorization_list['authorization_bearer'], 'Cookie': cookie}
    r = requests.post(url_block, verify=False, headers=user_agent, data=data, proxies=aurhorization_list['proxies'])
    flag = 0

    if r.status_code < 500:
        try:
            status = json.loads(r.text)['errors'][0]['message']
            if status == "You have already retweeted this Tweet.":
                print('Пост уже ретвитнут')
        except Exception as err:
            print(f'ОШИБКА В ФУНКЦИИ: {err}')
            flag += 1
            pass

        try:
            status = r.json()["retweeted"]
            if status == True:
                print('Успешно ретвитнул')
        except Exception as err:
            print(f'ОШИБКА В ФУНКЦИИ: {err}')
            flag += 1
            pass
    else:
        print(r.text)

def quote_tweet_post(aurhorization_list, message, tweet_status): #пример: https://twitter.com/JamesMelville/status/1516669369677406208
    url_block = "https://api.twitter.com/1.1/statuses/update.json"
    data = {"status": message, 'attachment_url': tweet_status}
    cookie = "ct0=%s; auth_token=%s" % (aurhorization_list['csrf_token'], aurhorization_list['auth_token'])
    user_agent = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0',
                  'X-Csrf-Token': aurhorization_list['csrf_token'], 'Content-Type': 'application/x-www-form-urlencoded',
                  'Authorization': aurhorization_list['authorization_bearer'], 'Cookie': cookie}
    r = requests.post(url_block, verify=False, headers=user_agent, data=data, proxies=aurhorization_list['proxies'])
    flag = 0

    if r.status_code < 500:
        try:
            status = json.loads(r.text)['text']
            if status == message:
                print('Успешно quote tweet')
        except Exception as err:
            print(f'ОШИБКА В ФУНКЦИИ: {err}')
            flag += 1
            pass

        try:
            status = json.loads(r.text)['errors'][0]['message']
            if status == "Status is a duplicate.":
                print('Quote tweet уже сделан')
        except Exception as err:
            print(f'ОШИБКА В ФУНКЦИИ: {err}')
            flag += 1
            pass
    else:
        print(r.text)

def follow_user(aurhorization_list, user_id):
    url_block = "https://api.twitter.com/1.1/friendships/create.json"
    data = {"user_id": user_id}
    cookie = "ct0=%s; auth_token=%s" % (aurhorization_list['csrf_token'], aurhorization_list['auth_token'])
    user_agent = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0',
                  'X-Csrf-Token': aurhorization_list['csrf_token'], 'Content-Type': 'application/x-www-form-urlencoded',
                  'Authorization': aurhorization_list['authorization_bearer'], 'Cookie': cookie}
    r = requests.post(url_block, verify=False, headers=user_agent, data=data, proxies=aurhorization_list['proxies'])
    flag = 0

    if r.status_code < 500:
        try:
            status = json.loads(r.text)['following']
            if status == True:
                print('Успешно подписан')
        except Exception as err:
            print(f'ОШИБКА В ФУНКЦИИ {inspect.getframeinfo(inspect.currentframe()).function}: ')
            flag += 1
            pass
    else:
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
    flag = 0

    if r.status_code < 500:
        try:
            status = json.loads(r.text)['text']
            if message in status:
                print('Успешно оставлен комментарий')
        except Exception as err:
            print(f'ОШИБКА В ФУНКЦИИ: {err}')
            flag += 1
            pass

        try:
            status = json.loads(r.text)['errors'][0]['message']
            if status == "Status is a duplicate.":
                print('Комментарий уже оставлен')
        except Exception as err:
            print(f'ОШИБКА В ФУНКЦИИ: {err}')
            flag += 1
            pass
    else:
        print(r.text)


if __name__ == '__main__':
    follow_user(auth, '1070099092246802432')
    retweet_post(auth, '1516706961894563846')
    quote_tweet_post(auth,'@CryptoGenres @Cometgollums2 @Gatuso5050' , 'https://twitter.com/SamuelXeus/status/1516706961894563846')
    like_post(auth, '1516706961894563846')
    comment_tweet(auth, '@CryptoGenres @Cometgollums2 @Gatuso5050', '1516706961894563846')
    print("--- %s seconds ---" % (time.time() - start_time))