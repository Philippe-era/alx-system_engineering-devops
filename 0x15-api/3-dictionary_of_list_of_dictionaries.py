#!/usr/bin/python3
"""DICTIONARY EXPORTING """
import json
import requests

if __name__ == "__main__":
    url_tocheck = "https://jsonplaceholder.typicode.com/"
    users = requests.get(url_tocheck + "users").json()

    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump({
            u.get("id"): [{
                "task": t.get("title"),
                "completed": t.get("completed"),
                "username": u.get("username")
            } for t in requests.get(url_tocheck + "todos",
                                    params={"userId": u.get("id")}).json()]
            for u in users}, jsonfile)
