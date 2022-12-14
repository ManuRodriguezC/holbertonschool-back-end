#!/usr/bin/python3
"""
This module start the conecction with API jsonplace
"""
import json
import requests


def gather():
    """
    This methos creted the dictionary of list of dictionaries of users
    """

    url_all = "https://jsonplaceholder.typicode.com/todos?"
    url_user = "https://jsonplaceholder.typicode.com/users?"

    response_all = requests.get(url_all)
    response_user = requests.get(url_user)

    all_json = response_all.json()
    user_json = response_user.json()

    all_dict = {}
    for user in user_json:
        list_date = []
        for dates in all_json:
            if user['id'] == dates['userId']:
                info_dict = {}
                info_dict['username'] = user['username']
                info_dict['task'] = dates['title']
                info_dict['completed'] = dates['completed']
                list_date.append(info_dict)
        all_dict[user['id']] = list_date

    JSON_file = json.dumps(all_dict)

    with open('todo_all_employees.json', 'w') as file:
        file.write(JSON_file)


if __name__ == '__main__':
    gather()
