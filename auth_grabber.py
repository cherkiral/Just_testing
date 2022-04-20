#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup
import re
import json
import urllib3
import urllib.parse
import sys
import argparse
import getpass

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

viewer_path = ''

def getTokens(proxies):
    user_agent = { 'User-Agent' : 'Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0', 'Referer' : 'https://twitter.com/sw.js' }
    url_base = "https://twitter.com/home?precache=1"
    r = requests.get(url_base, verify=False, headers=user_agent, proxies=proxies)
    soup = BeautifulSoup(r.text, "html.parser")
    js_with_bearer = ""
    for i in soup.find_all('link'):
        if i.get("href").find("/main") != -1:
            js_with_bearer = i.get("href")

    guest_token = re.findall(r'"gt=\d{19}', str(soup.find_all('script')[-1]), re.IGNORECASE)[0].replace("\"gt=","")
    print("[*] Js with Bearer token: %s" % js_with_bearer)
    print("[*] Guest token: %s" % guest_token)
    # Get Bearer token
    user_agent = { 'User-Agent' : 'Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0', 'Referer' : 'https://twitter.com/sw.js' }
    r = requests.get(js_with_bearer, verify=False, headers=user_agent, proxies=proxies)
    bearer = re.findall(r'",[a-z]="(.*)",[a-z]="\d{8}"', r.text, re.IGNORECASE)[0].split("\"")[-1]
    print("[*] Bearer: %s" % bearer)

    rt_path = re.search(r'queryId:"(.+?)",operationName:"Retweeters"', r.text).group(1).split('"')[-1]
    viewer_path = re.search(r'queryId:"(.+?)",operationName:"Viewer"', r.text).group(1).split('"')[-1]

    print("[*] rt_url: %s" % rt_path)
    authorization_bearer = "Bearer %s" % bearer
    return authorization_bearer,guest_token,rt_path,viewer_path

def getCSRFToken(guest_token, auth_token, authorization_bearer, proxies):
    # Get CSRF Token
    payload = '{"withCommunitiesMemberships":true,"withCommunitiesCreation":true,"withSuperFollowsUserFields":true}'
    url_session_token = "https://twitter.com/i/api/graphql/%s/Viewer?variables=%s" % (viewer_path, urllib.parse.quote_plus(payload))
    cookie = "ct0=%s; auth_token=%s" % (guest_token, auth_token)
    user_agent = { 'User-Agent' : 'Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0', 'Referer' : 'https://twitter.com/sw.js', 'X-Guest-Token' : guest_token, 'Content-Type' : 'application/json', 'Authorization' :  authorization_bearer, 'Cookie' : cookie  }
    r = requests.get(url_session_token, verify=False, headers=user_agent, proxies=proxies)
    csrf_token = r.cookies['ct0']
    print("[*] CSRF token: %s" % csrf_token)
    return csrf_token

def login(authorization_bearer, guest_token, username, password, email, proxies):
    # SSO login
    url_flow_1 = "https://twitter.com/i/api/1.1/onboarding/task.json?flow_name=login"
    url_flow_2 = "https://twitter.com/i/api/1.1/onboarding/task.json"
    # Flow 1
    data = {'' : ''}
    user_agent = { 'User-Agent' : 'Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0', 'Referer' : 'https://twitter.com/sw.js', 'X-Guest-Token' : guest_token, 'Content-Type' : 'application/json', 'Authorization' :  authorization_bearer  }
    r = requests.post(url_flow_1, verify=False, headers=user_agent, data=json.dumps(data), proxies=proxies)
    flow_token = json.loads(r.text)['flow_token']
    print("[*] flow_token: %s" % flow_token)

    # Flow 2
    data = {'flow_token' : flow_token, "subtask_inputs" : []}
    user_agent = { 'User-Agent' : 'Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0', 'Referer' : 'https://twitter.com/sw.js', 'X-Guest-Token' : guest_token, 'Content-Type' : 'application/json', 'Authorization' :  authorization_bearer  }
    r = requests.post(url_flow_2, verify=False, headers=user_agent, data=json.dumps(data), proxies=proxies)
    flow_token = json.loads(r.text)['flow_token']
    print("[*] flow_token: %s" % flow_token)

    # Flow 3
    data = {"flow_token": flow_token ,"subtask_inputs":[{"subtask_id":"LoginEnterUserIdentifierSSOSubtask","settings_list":{"setting_responses":[{"key":"user_identifier","response_data":{"text_data":{"result":username}}}],"link":"next_link"}}]}
    user_agent = { 'User-Agent' : 'Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0', 'Referer' : 'https://twitter.com/sw.js', 'X-Guest-Token' : guest_token, 'Content-Type' : 'application/json', 'Authorization' :  authorization_bearer  }
    r = requests.post(url_flow_2, verify=False, headers=user_agent, data=json.dumps(data), proxies=proxies)
    flow_token = json.loads(r.text)['flow_token']
    print("[*] flow_token: %s" % flow_token)


    if (json.loads(r.text)['subtasks'][0]['subtask_id'] == "LoginEnterAlternateIdentifierSubtask"):
        # Sometimes login alternate because unusual LoginEnterUserIdentifierSSOSubtask
        data = {"flow_token": flow_token, "subtask_inputs":[{"subtask_id":"LoginEnterAlternateIdentifierSubtask","enter_text":{"text": email,"link":"next_link"}}]}
        user_agent = { 'User-Agent' : 'Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0', 'Referer' : 'https://twitter.com/sw.js', 'X-Guest-Token' : guest_token, 'Content-Type' : 'application/json', 'Authorization' :  authorization_bearer  }
        r = requests.post(url_flow_2, verify=False, headers=user_agent, data=json.dumps(data), proxies=proxies)
        flow_token = json.loads(r.text)['flow_token']
        print("[*] flow_token: %s" % flow_token)


    # Flow 4
    data = {"flow_token": flow_token ,"subtask_inputs":[{"subtask_id":"LoginEnterPassword","enter_password":{"password":password,"link":"next_link"}}]}
    user_agent = { 'User-Agent' : 'Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0', 'Referer' : 'https://twitter.com/sw.js', 'X-Guest-Token' : guest_token, 'Content-Type' : 'application/json', 'Authorization' :  authorization_bearer  }
    r = requests.post(url_flow_2, verify=False, headers=user_agent, data=json.dumps(data), proxies=proxies)
    flow_token = json.loads(r.text)['flow_token']
    user_id = json.loads(r.text)['subtasks'][0]['check_logged_in_account']['user_id']
    print("[*] flow_token: %s" % flow_token)
    print("[*] user_id: %s" % user_id)

    # Flow 5 (and get auth_token)
    data = {"flow_token":flow_token,"subtask_inputs":[{"subtask_id":"AccountDuplicationCheck","check_logged_in_account":{"link":"AccountDuplicationCheck_false"}}]}
    user_agent = { 'User-Agent' : 'Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0', 'Referer' : 'https://twitter.com/sw.js', 'X-Guest-Token' : guest_token, 'Content-Type' : 'application/json', 'Authorization' :  authorization_bearer  }
    r = requests.post(url_flow_2, verify=False, headers=user_agent, data=json.dumps(data), proxies=proxies)
    flow_token = json.loads(r.text)['flow_token']
    auth_token = r.cookies['auth_token']
    print("[*] flow_token: %s" % flow_token)
    print("[*] auth_token: %s" % auth_token)
    return auth_token
