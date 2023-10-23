#!/usr/bin/python3
"""THIS IS THE TASK INFO"""
import requests
import sys

if __name__ == "__main__":
    url_tocheck = "https://jsonplaceholder.typicode.com/"
    user_network = requests.get(url_tocheck + "users/{}".format(sys.argv[1])).json()
    todos_check = requests.get(url_tocheck + "todos", params={"userId": sys.argv[1]}).json()

    done = [t.get("title") for t in todos_check if t.get("completed") is True]
    print("Employee {} is done with tasks({}/{}):".format(
        user_network.get("name"), len(done), len(todos_check)))
    [print("\t {}".format(c)) for c in done]
