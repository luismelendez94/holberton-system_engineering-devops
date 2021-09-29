#!/usr/bin/python3
""" Function that queries a Reddit API and returns the number of subscribers
    for a given subreddit. If an invalid subreddit is given, return 0. """
import requests


def number_of_subscribers(subreddit):
    """ Get the amount of subs """
    url = "https://www.reddit.com/r/" + subreddit + "/about.json"
    headers = 'Mozilla/5.0 (X11; Linux x86_64) ' \
              'AppleWebKit/537.36 (KHTML, like Gecko) ' \
              'Chrome/80.0.3987.87 Safari/537.36'

    response = requests.get(url, allow_redirects=False,
                            headers={'User-Agent': headers})

    if response.status_code != 200:
        return 0
    return response.json().get('data').get('subscribers')
