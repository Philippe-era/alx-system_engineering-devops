#!/usr/bin/python3
"""API IS IN PLACE FROM REDDIT"""
import requests
next_check = None


def recurse(subreddit, list_hot=[]):
    """returning top ten post titles recursively"""
    global next_check
    user_agent = {'User-Agent': 'api_advanced-project'}
    url_check = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    arguements = {'after': next_check}
    results = requests.get(url_check, params=arguements, headers=user_agent,
                           allow_redirects=False)

    if results.status_code == 200:
        next_check_data = results.json().get("data").get("next_check")
        if next_check_data is not None:
            next_check = next_check_data
            recurse(subreddit, list_hot)
        titles_list = results.json().get("data").get("children")
        for title_ in titles_list:
            list_hot.append(title_.get("data").get("title"))
        return list_hot
    else:
        return (None)
