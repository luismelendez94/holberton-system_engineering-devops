#!/usr/bin/python3
""" Recursive function that queries a Reddit API, parses the title of all hot articles,
    and prints a sorted count of given keywords """
import requests


def count_words(subreddit, word_list):
    """ Get the total of titles recursively """
    url = "https://www.reddit.com/r/" + subreddit + "/about.json"
    headers = {'user-agent': 'my-app/0.0.1'}

    response = requests.get(url, headers=headers)

    if response.status_code == 404:
        return 0
    else:
        print(response.status_code)
        return 1
