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
users_list = ['@' + user for user in users]

for i in range(5):
    users_list_temp = users_list
    rand_user = users_list[random.randint(0, len(users_list) - 1)]
    print(rand_user)
    users_list.pop(users_list.index(rand_user))

# for key in range(1, 200):
#     try:
#         print(key)
#         follow_user(data[f'{key}'], '1485307892672700421')
#         time.sleep(random.uniform(0, 3))
#         follow_user(data[f'{key}'], '4017596542')
#         time.sleep(random.uniform(0, 3))
#         retweet_post(data[f'{key}'], '1517443100628635648')
#         time.sleep(random.uniform(0, 3))
#         like_post(data[f'{key}'], '1517443100628635648')
#         time.sleep(random.uniform(0, 3))
#         comment_tweet(data[f'{key}'], '', '1517443100628635648')
#
#
#     except Exception as err:
#         print(f"ОШИБКА В ЦИКЛЕ: {err}")
#
# print("--- %s seconds ---" % (time.time() - start_time))