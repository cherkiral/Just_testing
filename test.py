from funcs import *
from pprint import pprint
import json
from auth_grabber import *

with open('auth_data.txt') as f:
    auth = json.load(f)

pprint(auth)