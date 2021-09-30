#!/usr/bin/python3
""" Function that queries a Reddit API and prints the titles of the
    first 10 hot posts listed for a given subreddit. """
import requests


def top_ten(subreddit):
    """ Get the total of subs """

    url = 'https://www.reddit.com/r/' + subreddit + '/.json?limit=10'
    headers = 'Mozilla/5.0 (X11; Linux x86_64) ' \
              'AppleWebKit/537.36 (KHTML, like Gecko) ' \
              'Chrome/80.0.3987.87 Safari/537.36'

    resp = requests.get(url, allow_redirects=False,
                        headers={'User-Agent': headers})

    if resp.status_code != 200:
        print('None')
    else:
        resp = resp.json().get('data')
        for chill in resp.get('children'):
            print(chill.get('data').get('title'))
