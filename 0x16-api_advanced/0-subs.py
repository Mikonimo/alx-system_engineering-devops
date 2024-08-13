#!/usr/bin/python3
"""queries the Reddit API and returns the number of subscribers
for a given subreddit"""
import requests


def num_subscribers(subreddit):
    """Queries the Reddit API"""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "python:subreddit.subscriber.counter:v1.0.0\
               (by /u/yourusername)"}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            return data["data"]["subscribers"]
        else:
            return 0
    except requests.RequestException:
        return 0
