#!/usr/bin/python3
""" odule for the main in verses the count """
import requests


def count_words(subreddit, word_list, new_after='',
                words_dict={}):

    word_list = map(lambda x: x.lower(), word_list)
    word_list = list(word_list)
# result from the request
    res = requests.get("https://www.reddit.com/r/{}/hot.json"
                       .format(subreddit),
                       headers={'User-Agent': 'Custom'},
                       params={'after': new_after},
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
#iterates thru the information
    for post in children:
        title = post.get('data', {}).get('title', '')
        for key_word in word_list:
            for word in title.lower().split():
                if key_word == word:
                    words_dict[key_word] = words_dict.get(key_word, 0) + 1

    new_after = response.get('after', None)
#if conditions
    if new_after is None:
        sorted_dict = sorted(words_dict.items(),
                             key=lambda x: x[1],
                             reverse=True)
#loops thru the sorted dictionary
        for initial in sorted_dict:
            if initial[1] != 0:
                print("{}: {}".format(initial[0], initial[1]))
        return
#will return the count words from the main .py
    return count_words(subreddit, word_list,
                       new_after, words_dict)
