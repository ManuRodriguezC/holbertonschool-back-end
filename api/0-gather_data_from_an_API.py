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

    url_all = "https://jsonplaceholder.typicode.com/todos?userId={}".format(
        argv[1])
    url_user = "https://jsonplaceholder.typicode.com/users?id={}".format(
        argv[1])

    response_all = requests.get(url_all)
    response_user = requests.get(url_user)

    all_json = response_all.json()
    user_json = response_user.json()
    comp, task = 0, 0

    for dates in all_json:
        task += 1
        if dates['completed'] is True:
            comp += 1

    name = user_json[0]['name']
    print("Employee {} is done with tasks({}/{}):".format(name, comp, task))
    for dates in all_json:
        if dates['completed'] is True:
            print(f"\t{dates['title']}")


if __name__ == '__main__':
    gather()
