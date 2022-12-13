#!/usr/bin/python3
"""
This module start the conecction with API jsonplace
"""
import requests
from sys import argv


def gather():
    """
    This methos return the tasks of the users
    """

    user_id = int(argv[1])
    url_all = "https://jsonplaceholder.typicode.com/todos"
    url_user = "https://jsonplaceholder.typicode.com/users"

    response_all = requests.get(url_all)
    response_user = requests.get(url_user)

    all_json = response_all.json()
    user_json = response_user.json()
    complete, task = 0, 0

    for dates in all_json:
        if dates['userId'] == user_id:
            task += 1
            if dates['completed'] is True:
                complete += 1

    user = user_json[user_id - 1]
    name = user['name']

    print(f"Employee {name} is done with tasks({complete}/{task}):")
    for dates in all_json:
        if dates['userId'] == user_id and dates['completed'] is True:
            print(f"\t{dates['title']}")


if __name__ == '__main__':
    gather()
