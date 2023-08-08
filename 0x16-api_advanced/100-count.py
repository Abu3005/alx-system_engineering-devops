#!/usr/bin/python3
"""
recurse a request, poor api
"""
from collections import defaultdict
import requests

base_url = "https://www.reddit.com/r/{}.json?limit=100"
h = requests.utils.default_headers()
headers = {'User-Agent': "ubuntu:noredditapp (by /u/noone)'"}
h.update(headers)


def count_words(subreddit, word_list, dico=defaultdict(int), after="start"):
    """
    the recursion
    """
    if not word_list:
        return
    url = base_url.format(subreddit)
    if after != "start":
        url += "&after={}".format(after)
    else:
        word_list = [word.lower() for word in word_list]
    r = requests.get(url, headers=h, allow_redirects=False)
    if r.status_code != 200:
        return
    for value in r.json()['data'].get('children', []):
        title = value['data']['title'].lower().split()
        for word in title:
            if word in word_list:
                dico[word] += 1
    after = r.json()['data'].get('after')
    if not after:
        if dico:
            tmp = ["{}: {:d}".format(k, dico[k]) for
                   k in sorted(dico, key=dico.get, reverse=True)]
            print("\n".join(tmp))
    else:
        return count_words(subreddit, word_list, dico, after)