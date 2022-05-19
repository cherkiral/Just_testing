from funcs import *
from pprint import pprint
import json
from auth_grabber import *
import itertools
import random
from threading import Thread
from pathlib import Path
import os

# start_time = time.time()
#
# accs_list = [i for i in range(1, 5)]
# comb_list = []
# perm_set = itertools.permutations(accs_list, 2)
# for i in perm_set:
#     comb_list.append(list(i))
# random.shuffle(comb_list)
#
#
#
# def follow_staright(comb_list, number):
#     print(comb_list[number])
#     time.sleep(0.5)
#
# def follow_async(comb_list):
#     for i in range(len(comb_list)):
#         th = Thread(target=follow_staright(comb_list, i), args=(i, ))
#         th.start()
#
#
# follow_async(comb_list)
#
#
# print("--- %s seconds ---" % (time.time() - start_time))

# with open('auth_data_temp.txt') as f:
#     data = json.load(f)
# with open('users_tag.txt') as f:
#     users = f.read().split()
#
# try:
#     comment_tweet(data[f'4'], 'heyyyy', 'abc')
# except Exception as err:
#     print(f"ОШИБКА В ЦИКЛЕ: {err}")

# url = 'https://twitter.com/account/access'
# proxies = {
#     "https": "http://t6CauBkh:AhDnyuC3@62.76.7.247:50782"
# }
#
# cookie = "ct0=%s; auth_token=%s" % ('1b2acb8f5375ea68838150c7319557af72cc81e18f7d84f2941424316bed375a1be7ca7dbec76942565cfe007ac38be368af242a8167b98bc86a24c265b122743c1c312bf89adbf59d39bc4c283209bd', '2edbeadb1b861cbf2d4b166c45687c5fabb64dbd')
# user_agent = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36',
#     'X-Csrf-Token': '1b2acb8f5375ea68838150c7319557af72cc81e18f7d84f2941424316bed375a1be7ca7dbec76942565cfe007ac38be368af242a8167b98bc86a24c265b122743c1c312bf89adbf59d39bc4c283209bd', 'Content-Type': 'application/x-www-form-urlencoded',
#     'Authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA', 'Cookie': cookie}
# r = requests.get(url, verify=False, headers=user_agent, proxies=proxies)
# print(r.text)
#
# path = os.getcwd()
# os.chdir('Project data')
#
#
#
# with open('follow.txt') as f:
#     b = []
#     for line in f.readlines():
#         b.append(line.rstrip())
# follow_list = [acc.split('\t') for acc in b]
#
# with open('twitter_id.txt') as f:
#     twitter_id_list = []
#     for line in f.readlines():
#         twitter_id_list.append(line.rstrip())
#
# with open('TagNumber.txt') as f:
#     tag_number_list = []
#     for line in f.readlines():
#         tag_number_list.append(line.rstrip())
#
# for project_number in range(len(follow_list)):
#     for my_acc in range(1, 5):
#         for acc_to_follow in follow_list[project_number]:
#             follow_user(data[f'{key}'], acc_to_follow)
#
#         retweet_post(data[f'{key}'], twitter_id_list[project_number])
#
#         like_post(data[f'{key}'], twitter_id_list[project_number])
#
#         for i in range(tag_number_list[project_number]):
#             rand_user = users_list[random.randint(0, len(users_list) - 1)]
#             rand_user_str += rand_user + ' '
#             users_list.pop(users_list.index(rand_user))
#         comment_tweet(data[f'{key}'], rand_user_str, twitter_id_list[project_number])

os.chdir('Project data')

with open('follow.txt') as f:
    print(f.read().split())