#!/usr/bin/python3
"""EVERYTHING EXPORTED YEAH"""
import csv
import requests
import sys

if __name__ == "__main__":
    user_id = sys.argv[1]
    www = "https://jsonplaceholder.typicode.com/"
    user_check = requests.get(www + "users/{}".format(user_id)).json()
    username = user_check.get("username")
    list1 = requests.get(www + "todos", params={"userId": user_id}).json()

    with open("{}.csv".format(user_id), "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        [writer.writerow(
            [user_id, username, t.get("completed"), t.get("title")]
         ) for t in list1]
