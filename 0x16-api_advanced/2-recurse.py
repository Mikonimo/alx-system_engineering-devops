#!/usr/bin/python3
"""Recursively queries the Reddit API and returns a list
of titles of all hot articles for a given subreddit"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """Recursively queries the Reddit API"""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "python:subreddit.recurse:v1.0.0\
               (by /u/yourusername)"}
    params = {"limit": 100, "after": after}

    try:
        response = requests.get(url, headers=headers, params=params,
                                allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            children = data["data"]["children"]
            after = data["data"]["after"]

            if not children:
                return hot_list if hot_list else None

            hot_list.extend([child["data"]["title"] for child in children])

            if after is None:
                return hot_list
            else:
                return recurse(subreddit, hot_list, after)
        else:
            return None
    except requests.RequestException:
        return None
