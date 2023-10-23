#!/usr/bin/python3
"""THIS IS THE TASK INFO"""
import requests
import sys

if __name__ == "__main__":
    url_1 = "https://jsonplaceholder.typicode.com/"
    user_network = requests.get(url_1 + "users/{}".format(sys.argv[1])).json()
    list_1 = requests.get(url_1 + "todos", params={"userId": sys.argv[1]}).json()
    done = [t.get("title") for t in list_1 if t.get("completed") is True]
    print("Employee {} is done with tasks({}/{}):".format(
        user_network.get("name"), len(done), len(list_1)))
    [print("\t {}".format(c)) for c in done]
