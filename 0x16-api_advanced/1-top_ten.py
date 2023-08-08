#!/usr/bin/python3
"""
Using the capacity to append.json to whatever link on reddit
"""
import requests


def top_ten(subreddit):
    """
    get the title of the 10 hot posts on a given subreddit

    Argument:
       subreddit: a subreddit
    """
    url = "https://www.reddit.com/r/{}.json?limit=10&t=day".format(subreddit)
    h = requests.utils.default_headers()
    headers = {'User-Agent': "ubuntu:noredditapp (by /u/noone)'"}
    h.update(headers)
    r = requests.get(url, headers=h).json()
    if not r.get('data', {}).get('children', []):
        print("None")
    else:
        for value in r['data']['children']:
            print(value['data']['title'])