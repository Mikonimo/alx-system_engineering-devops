#!/usr/bin/python3
"""Prints the titles of the first 10 hot posts
or a given subreddit"""
import requests


def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts"""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "python:subreddit.top.ten:v1.0.0\
               (by /u/yourusername)"}
    params = {"limit": 10}

    try:
        response = requests.get(url, headers=headers,
                                params=params, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            posts = data["data"]["children"]
            for post in posts:
                print(post["data"]["title"])
        else:
            print(None)
    except requests.RequestException:
        print(None)
