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

    url_all = "https://jsonplaceholder.typicode.com/todos?userId="
    url_user = "https://jsonplaceholder.typicode.com/users?id="

    response_all = requests.get(url_all + argv[1])
    response_user = requests.get(url_user + argv[1])

    all_json = list(response_all.json())
    user_json = list(response_user.json())
    comp, task = 0, 0
    list_task = []

    for dates in all_json:
        task += 1
        if dates['completed'] is True:
            comp += 1
            list_task.append(dates['title'])

    name = user_json[0]['name']
    print("Employee {} is done with tasks({}/{}):".format(name, comp, task))
    for task in list_task:
        print("\t" + task)


if __name__ == '__main__':
    gather()
