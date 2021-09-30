#!/usr/bin/python3
""" Recursive function that queries a Reddit API and returns a list containing
    the titles of all hot hot articles for a given subreddit. If no results are
    found for the given subreddit, the function should return None. """
import requests


def recurse(subreddit, hot_list=[], after="", count=0):
    """ Get the total of titles recursively """

    url = 'https://www.reddit.com/r/' + subreddit + '/hot/.json'
    headers = {'user-agent': 'my-app/0.0.1'}

    parameters = {
        "after": after,
        "count": count,
        "limit": 100
    }

    resp = requests.get(url, allow_redirects=False,
                        headers=headers, params=parameters)

    if resp.status_code != 200:
        return None
    else:
        result = resp.json().get('data')
        after = result.get('after')
        count += result.get('dist')

        for chill in result.get('children'):
            hot_list.append(chill.get('data').get('title'))

        if after is not None:
            return recurse(subreddit, hot_list, after, count)

        return hot_list
