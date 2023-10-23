#!/usr/bin/python3
"""THIS IS THE TASK INFO"""
import requests
import sys

if __name__ == "__main__":
    www = "https://jsonplaceholder.typicode.com/"
    user_network = requests.get(www + "users/{}".format(sys.argv[1])).json()
    list1 = requests.get(www + "todos", params={"userId": sys.argv[1]}).json()
    done = [t.get("title") for t in list1 if t.get("completed") is True]
    print("Employee {} is done with tasks({}/{}):".format(
        user_network.get("name"), len(done), len(list1)))
    [print("\t {}".format(c)) for c in done]
