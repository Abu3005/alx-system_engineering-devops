#!/usr/bin/python3
"""
This is module 0-subs.
I query the reddit api without login
"""
import requests


def number_of_subscribers(subreddit):
    """
    get number of subscribers on a subreddit

    Argument:
        subreddit: a subreddit name

    Return:
        the number of subscribers, default to 0
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    h = requests.utils.default_headers()
    headers = {'User-Agent': "ubuntu:noredditapp (by /u/noone)'"}
    h.update(headers)
    r = requests.get(url, headers=h).json()
    answer = r.get('data', {}).get('subscribers')
    if not answer:
        return 0
    else:
        return answer