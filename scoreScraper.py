#!/usr/bin/env python3
# program scraps pro-football-reference.com for NFL scores

import requests
import pyperclip
from bs4 import BeautifulSoup

# accepts user input for year and week and uses input for URL of web page
year = input("Enter Year: ")
week = input("Enter Week: ")
url = ("https://www.pro-football-reference.com/years/" + year + "/week_" + week + ".htm")

# downloads web page and creates beautiful soup object
page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")

# searches beautiful soup object and locates specific tags
games = soup.find('div', class_="game_summaries")
scores = games.find_all('table', class_='teams')

date = ''
homeTeam = ''
homeScore = ''
awayTeam = ''
awayScore = ''
final = ''

# loops through soup and assigns to variables
i = 0
while i < len(scores):
    # breaks down text information by using splitlines and inserts into list named 'game'
    game = scores[i].get_text().splitlines()
    # assigns index of game to a variable
    date = game[2]
    # further breaks down index 4 of 'game' and assign to 'home'. assigns last index of home to 'hometeam' variable
    home = game[4].split()
    homeTeam = home[-1]
    homeScore = game[5]
    # same as previous but assigns 'awayteam'
    away = game[11].split()
    awayTeam = away[-1]
    awayScore = game[12]

    # inserts variables into string formatted for SQL insert statement
    sql = ("('" + date + "', '" + homeTeam + "', " + homeScore + ", '" + awayTeam + "', " + awayScore + "),")

    # checks to see if 'final' string is empty and adds to 'final' string
    if len(final) == 0:
        final = sql
    else:
        final = (final + "\n"
                 + sql)
    i += 1

# sends 'final' to clipboard
pyperclip.copy(final)
