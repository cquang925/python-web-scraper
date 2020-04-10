#!/usr/bin/env python3
# web scrapper used to scrape ESPN for NFL players

import requests
from bs4 import BeautifulSoup
import pyperclip

team = input("Enter Team: ")
URL = ("https://www.espn.com/nfl/team/roster/_/name/" + team)

page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")
information = soup.find_all(class_="Table__TD")

firstName = ''
lastName = ''
num = ''
position = ''
age = ''
height = ''
weight = ''
experience = ''
college = ''
sql = ''
final = ''
team = team.upper()

i = 0
while i < len(information):
    i += 1
    n = information[i].get_text()
    name = n.split(' ')
    firstName = name[0]
    if len(name) >= 3:
        lastNum = name[2]
        lastName = name[1]
    else:
        lastNum = name[1]
        lastName = ''.join([j for j in lastNum if not j.isdigit()])
    num = ''.join([k for k in lastNum if k.isdigit()])
    i += 1
    position = information[i].get_text()
    i += 1
    age = information[i].get_text()
    i += 1
    h = information[i].get_text()
    height = h[:1] + ' ft' + h[2:-1] + ' in'
    i += 1
    weight = information[i].get_text()
    weight = weight[:-4]
    i += 1
    e = information[i].get_text()
    if e == 'R':
        experience = '0'
    else:
        experience = e
    i += 1
    college = information[i].get_text()
    i += 1

    sql = ("('" + firstName + "', '" + lastName + "', '" + team + "', " + num + ", '" + position + "', '" + height +
           "', " + weight + ", " + experience + ", '" + college + "'),")

    if len(final) == 0:
        final = sql
    else:
        final = (final + "\n"
                 + sql)

pyperclip.copy(final)
