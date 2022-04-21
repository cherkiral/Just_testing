from funcs import *
from pprint import pprint
import json
from auth_grabber import *


def getting_auth():
    data = {}
    numbers_list = []
    with open('twitter_data.txt') as f:
        for line in f:
            raw_data = line.rstrip('\n').split(';')
            number = raw_data[0]
            username = raw_data[1]
            password = raw_data[2]
            email = raw_data[3]
            proxy = raw_data[4]
            proxy_dict = {
                'https': f'http://{proxy}'
            }
            data[f'{number}'] = {
                'username': username,
                'password': password,
                'email': email,
                'proxy': proxy_dict
            }
            numbers_list.append(number)

    with open('auth_parsing.txt', 'w') as f:
        json.dump(data, f)

    def full_auth(number, parsed_data):
        authorization_bearer, guest_token, rt_path, viewer_path = getTokens(parsed_data[f'{number}']['proxy'])
        auth_token = login(authorization_bearer, guest_token, parsed_data[f'{number}']['username'], parsed_data[f'{number}']['password'], parsed_data[f'{number}']['email'], parsed_data[f'{number}']['proxy'])
        csrf_token = getCSRFToken(guest_token, auth_token, authorization_bearer, parsed_data[f'{number}']['proxy'])
        return auth_token, csrf_token, authorization_bearer

    auth = {}
    error_accs = []
    for i in range(len(data)):
        proxy = data[f'{numbers_list[i]}']['proxy']
        print(f'Account {numbers_list[i]}')
        try:
            auth_token, csrf_token, authorization_bearer = full_auth(numbers_list[i], data)
            auth[f'{numbers_list[i]}'] = {
                'auth_token': auth_token,
                'csrf_token': csrf_token,
                'authorization_bearer': authorization_bearer,
                'proxies': proxy
            }
            with open('auth_data_temp.txt', 'w') as f:
                json.dump(auth, f)
        except Exception:
            print(f'Аккаунт {numbers_list[i]}: ОШИБКА')
            error_accs.append(numbers_list[i])
            auth[f'{numbers_list[i]}'] = {
                'auth_token': 'auth_token',
                'csrf_token': 'csrf_token',
                'authorization_bearer': 'authorization_bearer',
                'proxies': proxy
            }
            continue

    with open('error_accs.txt', 'w') as f:
        json.dump(auth, f)

getting_auth()