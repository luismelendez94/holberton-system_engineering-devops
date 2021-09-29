#!/usr/bin/python3
""" Function that queries a Reddit API and returns the number of subscribers
    for a given subreddit. If an invalid subreddit is given, return 0. """
import requests


def number_of_subscribers(subreddit):
    """ Get the amount of subs """
    response = requests.get("https://www.reddit.com/r/" + subreddit + ".json")

    print(response)

    return 0
