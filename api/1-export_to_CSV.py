#/!usr/bin/python3
"""
This module start the conecction with API jsonplace
"""
import requests
from sys import argv
import csv


def gather():
    """
    This methos return the tasks of the users
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
    id = user_json[0]['id']
    list_date = []
    
    for date in all_json:
        dates = f'{id},{name},{date["completed"]},{date["title"]}'
        list_date.append(dates)
    for date in list_date:
        print(date)
    
    with open('2.csv', 'w', encoding='UTF8') as file:
        writer = csv.writer(file)
        
        writer.writerow(list_date)

if __name__ == '__main__':
    gather()
