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

    url_all = f"https://jsonplaceholder.typicode.com/todos?userId={argv[1]}"
    url_user = f"https://jsonplaceholder.typicode.com/users?id={argv[1]}"

    response_all = requests.get(url_all)
    response_user = requests.get(url_user)

    all_json = response_all.json()
    user_json = response_user.json()
    complete, task = 0, 0

    for dates in all_json:
        task += 1
        if dates['completed'] is True:
            complete += 1

    name = user_json[0]['name']
    print(f"Employee {name} is done with tasks({complete}/{task}):")
    for dates in all_json:
        if dates['completed'] is True:
            print(f"\t{dates['title']}")


if __name__ == '__main__':
    gather()
