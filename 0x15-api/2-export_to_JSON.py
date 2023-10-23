#!/usr/bin/python3
"""EXPORTS INFO TO JSON"""
import json
import requests
import sys

if __name__ == "__main__":
    user_id = sys.argv[1]
    url_1 = "https://jsonplaceholder.typicode.com/"
    user_check = requests.get(url_1 + "users/{}".format(user_id)).json()
    username = user_check.get("username")
    list_1 = requests.get(url_1 + "todos", params={"userId": user_id}).json()

    with open("{}.json".format(user_id), "w") as jsonfile:
        json.dump({user_id: [{
                "task": t.get("title"),
                "completed": t.get("completed"),
                "username": username
            } for t in list_1]}, jsonfile)
