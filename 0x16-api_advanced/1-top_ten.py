#!/usr/bin/python3
"""Module for task 1"""

import requests

def top_ten(subreddit):
    """Queries the Reddit API and prints the titles of the first 10 hot posts
    for a given subreddit. If the subreddit is invalid, prints None."""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "My-User-Agent"}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            posts = response.json().get("data", {}).get("children", [])
            for post in posts[:10]:
                print(post.get("data", {}).get("title", ""))
        else:
            print(None)
    except requests.exceptions.RequestException:
        print(None)
