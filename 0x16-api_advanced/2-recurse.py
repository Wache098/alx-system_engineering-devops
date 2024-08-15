#!/usr/bin/python3
"""Module for task 2"""

import requests

def recurse(subreddit, hot_list=[]):
    """Queries the Reddit API recursively and returns a list of all hot article titles
    for a given subreddit."""
    
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "My-User-Agent"}
    
    if not hot_list:
        hot_list = []
    
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code != 200:
            return None
        
        data = response.json().get("data", {})
        children = data.get("children", [])
        
        if not children:
            return hot_list
        
        hot_list.extend([post.get("data", {}).get("title", "") for post in children])
        
        next_page = data.get("after")
        if next_page:
            next_url = f"{url}?after={next_page}"
            return recurse(subreddit, hot_list=hot_list)
        else:
            return hot_list

    except requests.exceptions.RequestException:
        return None
