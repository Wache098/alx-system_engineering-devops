#!/usr/bin/python3
"""Module for task 100"""

import requests
import re
from collections import Counter

def count_words(subreddit, word_list, after=None):
    """Queries the Reddit API recursively and counts the occurrences of keywords in hot articles' titles."""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "My-User-Agent"}
    
    # Define a Counter to hold the counts of each word
    counts = Counter()
    
    if not word_list:
        return
    
    # Process the response
    try:
        params = {'after': after} if after else {}
        response = requests.get(url, headers=headers, params=params, allow_redirects=False)
        if response.status_code != 200:
            return
        
        data = response.json().get("data", {})
        children = data.get("children", [])
        next_page = data.get("after")
        
        # Update the counts for each title
        for post in children:
            title = post.get("data", {}).get("title", "").lower()
            for word in word_list:
                # Use regex to count exact matches for each word
                count = len(re.findall(rf'\b{re.escape(word.lower())}\b', title))
                counts[word.lower()] += count
        
        # Recur if there's another page
        if next_page:
            count_words(subreddit, word_list, after=next_page)
        else:
            # Print the sorted results
            for word, count in sorted(counts.items(), key=lambda x: (-x[1], x[0])):
                print(f"{word}: {count}")

    except requests.exceptions.RequestException:
        return
