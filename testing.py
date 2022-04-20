from funcs import *
from pprint import pprint
import json
from auth_grabber import *

data = {}
count = 0
with open('twitter_data.txt') as f:
    for line in f:
        raw_data = line.rstrip('\n').split(';')
        username = raw_data[0]
        password = raw_data[1]
        email = raw_data[2]
        proxy = raw_data[3]
        proxy_dict = {
            'https': f'http://{proxy}'
        }
        data[f'{count + 1}'] = {
            'username': username,
            'password': password,
            'email': email,
            'proxy': proxy_dict
        }
        count += 1

number = 1

def full_auth(number, parsed_data):
    authorization_bearer, guest_token, rt_path, viewer_path = getTokens(parsed_data[f'{number}']['proxy'])
    auth_token = login(authorization_bearer, guest_token, parsed_data[f'{number}']['username'], parsed_data[f'{number}']['password'], parsed_data[f'{number}']['email'], parsed_data[f'{number}']['proxy'])
    csrf_token = getCSRFToken(guest_token, auth_token, authorization_bearer, parsed_data[f'{number}']['proxy'])
    return auth_token, csrf_token, authorization_bearer

count = 1
auth_data = {}

for i in range(len(data)):
    proxy = data[f'{count}']['proxy']
    auth_token, csrf_token, authorization_bearer = full_auth(count, data)
    auth[f'{count}'] = {
        'auth_token': auth_token,
        'csrf_token': csrf_token,
        'authorization_bearer': authorization_bearer,
        'proxies': proxy
    }
    count += 1
with open('auth_data.txt', 'w') as f:
    json.dump(auth, f)
