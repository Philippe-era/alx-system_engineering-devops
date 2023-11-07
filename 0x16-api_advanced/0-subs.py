#!/usr/bin/python3
"Subscriber count thru this line "
#import
import requests


def number_of_subscribers(subreddit):
    link = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    title_link = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(link, title_link=title_link, allow_redirects=False)
    data = response.json()
    if response.status_code != 200:
        return 0
    else:
        return data['data']['subscribers']

