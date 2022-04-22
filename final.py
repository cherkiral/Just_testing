from funcs import *
from pprint import pprint
import json
from auth_grabber import *
import random
import time
import sys

start_time = time.time()

with open('auth_data_temp.txt') as f:
    data = json.load(f)
with open('users_tag.txt') as f:
    users = f.read().split()


for key in range(1, 200):
    users_list = ['@' + user for user in users]
    rand_user_str = ''
    try:
        print(key)
        follow_user(data[f'{key}'], '1500259433674416130')

        follow_user(data[f'{key}'], '1507713106469961734')

        retweet_post(data[f'{key}'], '1517387092711596034')

        like_post(data[f'{key}'], '1517387092711596034')

        for i in range(3):
            rand_user = users_list[random.randint(0, len(users_list) - 1)]
            rand_user_str += rand_user + ' '
            users_list.pop(users_list.index(rand_user))
        comment_tweet(data[f'{key}'], rand_user_str, '1517387092711596034')


    except Exception as err:
        print(f"ОШИБКА В ЦИКЛЕ: {err}")

print("--- %s seconds ---" % (time.time() - start_time))

#time.sleep(random.uniform(0, 1))