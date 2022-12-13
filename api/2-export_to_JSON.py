#!/usr/bin/python3
"""
This module start the conecction with API jsonplace
"""
import json
import requests
from sys import argv


def gather():
    """
    This methos return the tasks of the users in json file
    """

    url_all = "https://jsonplaceholder.typicode.com/todos?"
    url_user = "https://jsonplaceholder.typicode.com/users?"
    argv_all = {'userId': argv[1]}
    argv_user = {'id': argv[1]}

    response_all = requests.get(url_all, params=argv_all)
    response_user = requests.get(url_user, params=argv_user)

    all_json = response_all.json()
    user_json = response_user.json()

    name = user_json[0]['username']

    all_dict = {}
    list_date = []
    for date in all_json:
        info_dict = {}
        info_dict['task'] = date['title']
        info_dict['completed'] = date['completed']
        info_dict['username'] = name
        list_date.append(info_dict)
    all_dict[argv[1]] = list_date

    JSON_date = json.dumps(all_dict)

    with open('{}.json'.format(argv[1]), 'w') as file:
        file.write(JSON_date)


if __name__ == '__main__':
    gather()
