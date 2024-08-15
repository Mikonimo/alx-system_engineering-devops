#!/usr/bin/python3
"""Prints the titles of the first 10 hot posts
or a given subreddit"""

import requests

def top_ten(subreddit):
    # Reddit API endpoint for hot posts
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"

    # Custom User-Agent to avoid Too Many Requests error
    headers = {'User-Agent': 'MyBot/0.0.1'}

    # Query parameters
    params = {'limit': 10}

    try:
        # Make the API request
        response = requests.get(url, headers=headers, params=params, allow_redirects=False)

        # Check if the subreddit is valid
        if response.status_code == 200:
            data = response.json()
            posts = data['data']['children']

            # Print the titles of the first 10 hot posts
            for post in posts:
                print(post['data']['title'])
        else:
            print(None)

    except requests.RequestException:
        print(None)
