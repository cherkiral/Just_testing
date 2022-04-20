from funcs import *
from pprint import pprint
import json
from auth_grabber import *

with open('auth_data.txt') as f:
    data = json.load(f)

for key in data:
    print(key)
    post_tweet(data[key], 'I did it finally')