#!/usr/bin/python3
""" Function that queries a Reddit API and prints the titles of the
    first 10 hot posts listed for a given subreddit. """
import requests


def top_ten(subreddit):
    """ Get the total of subs """
    url = "https://www.reddit.com/r/" + subreddit + "/about.json"
    headers = {'user-agent': 'my-app/0.0.1'}

    response = requests.get(url, headers=headers)

    if response.status_code == 404:
        return 0
    else:
        print(response.status_code)
        return 1
