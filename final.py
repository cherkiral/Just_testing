from funcs import *
from pprint import pprint
import json
from auth_grabber import *
import random
import time

start_time = time.time()

with open('auth_data_temp.txt') as f:
    data = json.load(f)


for key in data:
    print(key)
    follow_user(data[f'{key}'], '1515728847030923268')
    time.sleep(random.uniform(0, 1))
    follow_user(data[f'{key}'], '1479210745372020737')
    time.sleep(random.uniform(0, 1))
    follow_user(data[f'{key}'], '634075747')
    time.sleep(random.uniform(0, 1))
    retweet_post(data[f'{key}'], '1516778713622319111')
    time.sleep(random.uniform(0, 1))
    like_post(data[f'{key}'], '1516778713622319111')
    time.sleep(random.uniform(0, 1))
    comment_tweet(data[f'{key}'], '@DittoDegen @SQester @theJazzified', '1516778713622319111')
    time.sleep(random.uniform(0, 1))

print("--- %s seconds ---" % (time.time() - start_time))