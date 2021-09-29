#!/usr/bin/python3
""" Recursive function that queries a Reddit API and returns a list containing
    the titles of all hot hot articles for a given subreddit. If no results are
    found for the given subreddit, the function should return None. """
import requests


def recursive(subreddit, hot_list=[]):
    """ Get the total of titles recursively """
    url = "https://www.reddit.com/r/" + subreddit + "/about.json"
    headers = {'user-agent': 'my-app/0.0.1'}

    response = requests.get(url, headers=headers)

    if response.status_code == 404:
        return 0
    else:
        print(response.status_code)
        return 1
