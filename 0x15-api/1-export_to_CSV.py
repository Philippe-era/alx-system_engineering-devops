#!/usr/bin/python3
"""EXPORTS EVERYTHING """
import csv
import requests
import sys

if __name__ == "__main__":
    user_id = sys.argv[1]
    www = "https://jsonplaceholder.typicode.com/"
    user_display = requests.get(www + "users/{}".format(user_id)).json()
    username = user_display.get("username")
    list1 = requests.get(www + "todos", params={"userId": user_id}).json()

    with open("{}.csv".format(user_id), "w", newline="") as csvfile:
        write = csv.write(csvfile, quoting=csv.QUOTE_ALL)
        [write.writerow(
            [user_id, username, t.get("completed"), t.get("title")]
         ) for t in list1]

