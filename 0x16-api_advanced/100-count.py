#!/usr/bin/python3
"""Recursively queries the Reddit API, parses the title of all hot articles,
    and prints a sorted count of given keywords (case-insensitive)."""
from collections import Counter
import requests


def count_words(subreddit, word_list, after=None, word_counter=None):
    """Recursively queries the Reddit API"""
    if word_counter is None:
        word_counter = Counter()

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "python:subreddit.keyword.count:v1.0.0\
               (by /u/yourusername)"}
    params = {"limit": 100, "after": after}

    try:
        response = requests.get(url, headers=headers, params=params,
                                allow_redirects=False)
        if response.status_code != 200:
            return

        data = response.json()
        children = data["data"]["children"]
        after = data["data"]["after"]

        if not children:
            return

        # Prepare word_list for case-insensitive matching
        lower_word_list = [word.lower() for word in word_list]

        # Process titles and update the counter
        for child in children:
            title = child["data"]["title"].lower().split()
            filtered_words = [word for word in title if word in
                              lower_word_list]
            word_counter.update(filtered_words)

        # Recursive call if there's a next page
        if after:
            count_words(subreddit, word_list, after, word_counter)
        else:
            # Print the sorted results
            for word, count in sorted(word_counter.items(),
                                      key=lambda x: (-x[1], x[0])):
                if count > 0:
                    print(f"{word}: {count}")

    except requests.RequestException:
        return
