#!/usr/bin/python3
"""
recurse a request, poor api
"""
import requests


base_url = "https://www.reddit.com/r/{}.json?limit=100"
h = requests.utils.default_headers()
headers = {'User-Agent': "ubuntu:noredditapp (by /u/noone)'"}
h.update(headers)


def recurse(subreddit, hot_list=[], after="start"):
    """
    the recursion
    """
    url = base_url.format(subreddit)
    if after != "start":
        url += "&after={}".format(after)
    r = requests.get(url, headers=h, allow_redirects=False)
    if r.status_code != 200:
        return None
    for value in r.json()['data'].get('children', []):
        hot_list.append(value['data']['title'])
    after = r.json()['data'].get('after')
    if not after:
        return hot_list
    return (recurse(subreddit, hot_list, after))