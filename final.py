from funcs import *
from pprint import pprint
import json
from auth_grabber import *
import random
import time
import sys
import os

start_time = time.time()

with open('auth_data_temp.txt') as f:
    data = json.load(f)
with open('users_tag.txt') as f:
    users = f.read().split()

path = os.getcwd()
os.chdir('Project data')



with open('follow.txt') as f:
    b = []
    for line in f.readlines():
        b.append(line.rstrip())
follow_list = [acc.split('\t') for acc in b]

with open('twitter_id.txt') as f:
    twitter_id_list = []
    for line in f.readlines():
        twitter_id_list.append(line.rstrip())

with open('TagNumber.txt') as f:
    tag_number_list = []
    for line in f.readlines():
        tag_number_list.append(line.rstrip())

def only_follow_all(one, two):
    with open('follow.txt') as f:
        accs_list = f.read().split()

    for i in accs_list:
        for key in range(one, two):
            print(f'Аккаунт {key} подписывается на {i}')
            follow_user(data[f'{key}'], i)
            print()
            time.sleep(random.uniform(0, 1))

def final(one, two):
    for project_number in range(len(follow_list)):

        for key in range(one, two):
            users_list = ['@' + user for user in users]
            rand_user_str = ''

            print(key)

            retweet_post(data[f'{key}'], twitter_id_list[project_number])

            like_post(data[f'{key}'], twitter_id_list[project_number])

            for i in range(int(tag_number_list[project_number])):
                rand_user = users_list[random.randint(0, len(users_list) - 1)]
                rand_user_str += rand_user + ' '
                users_list.pop(users_list.index(rand_user))
            comment_tweet(data[f'{key}'], rand_user_str, twitter_id_list[project_number])
            time.sleep(random.uniform(0, 1))

only_follow_all(1, 200)
only_follow_all(401, 800)
final(1, 200)
final(401, 800)


print("--- %s seconds ---" % (time.time() - start_time))

#time.sleep(random.uniform(0, 1))

# for key in range(191, 192):
#     users_list = ['@' + user for user in users]
#     rand_user_str = ''
#     try:
#         print(key)
#
#         follow_user(data[f'{key}'], '1507713106469961734')
#
#         retweet_post(data[f'{key}'], '1517387092711596034')
#
#         like_post(data[f'{key}'], '1517387092711596034')
#
#         for i in range(3):
#             rand_user = users_list[random.randint(0, len(users_list) - 1)]
#             rand_user_str += rand_user + ' '
#             users_list.pop(users_list.index(rand_user))
#         comment_tweet(data[f'{key}'], rand_user_str, '1517387092711596034')
#
#
#
#     except Exception as err:
#         print(f"ОШИБКА В ЦИКЛЕ: {err}")