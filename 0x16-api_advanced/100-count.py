#!/usr/bin/python3
""" Module for the matter at hand """
import requests


def count_words(subreddit, listed_words, latest='',
                dictionary_words={}):

    listed_words = map(lambda x: x.lower(), listed_words)
    listed_words = list(listed_words)

    res = requests.get("https://www.reddit.com/r/{}/hot.json"
                       .format(subreddit),
                       headers={'User-Agent': 'Custom'},
                       params={'after': latest},
                       allow_redirects=False)

    if res.status_code != 200:
        return

    try:
        response = res.json().get('data', None)

        if response is None:
            return
    except ValueError:
        return

    children = response.get('children', [])

    for position in children:
        title = position.get('data', {}).get('title', '')
        for important_word in listed_words:
            for word in title.lower().split():
                if important_word == word:
                    dictionary_words[important_word] = dictionary_words.get(important_word, 0) + 1

    latest = response.get('after', None)

    if latest is None:
        sorted_dict = sorted(dictionary_words.items(),
                             key=lambda x: x[1],
                             reverse=True)

        for initial in sorted_dict:
            if initial[1] != 0:
                print("{}: {}".format(initial[0], initial[1]))
        return

    return count_words(subreddit, listed_words,
                       latest, dictionary_words)
