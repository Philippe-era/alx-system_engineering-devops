#!/usr/bin/python3
"""EXPORTS EVERYTHING """
import csv
import requests
import sys

if __name__ == "__main__":
    user_id = sys.argv[1]
    url_tocheck = "https://jsonplaceholder.typicode.com/"
    user_display = requests.get(url_tocheck + "users/{}".format(user_id)).json()
    username = user_display.get("username")
    todos_check = requests.get(url_tocheck + "todos", params={"userId": user_id}).json()

    with open("{}.csv".format(user_id), "w", newline="") as csvfile:
        write = csv.write(csvfile, quoting=csv.QUOTE_ALL)
        [write.writerow(
            [user_id, username, t.get("completed"), t.get("title")]
         ) for t in todos]

