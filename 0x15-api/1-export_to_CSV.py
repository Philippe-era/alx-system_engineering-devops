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
        write_file = csv.write_file(csvfile, quoting=csv.QUOTE_ALL)
        [write_file.writerow(
            [user_id, username, t.get("completed"), t.get("title")]
         ) for t in todos]

