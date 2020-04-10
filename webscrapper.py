#!/usr/bin/env python3
# program scrapes fftoday.com for football statics

import requests
from bs4 import BeautifulSoup
import pyperclip

# accepts user input and inserts input into URL
year = input("Enter Year: ")
week = input("Enter Week: ")
position = input("Enter Position (10 = QB, 20 = RB, 30 = WR, 40 = TE, 80 = K, 99 = DEF): ")
pageNum = input('Enter Page: ')
URL = ("https://fftoday.com/stats/playerstats.php?Season=" + year + "&GameWeek=" + week +
       "&PosID=" + position + "&LeagueID=193033&order_by=FFPts&sort_order=DESC&cur_page=" + pageNum)

# downloads the web page and creates a beautiful soup object. searches object for specific tag and class
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')
statistics = soup.find_all('td', class_='sort1')

rank = ''
fName = ''
lName = ''
team = ''
gp = ''
comp = ''
pass_att = ''
pass_yard = ''
pass_td = ''
inter = ''
rush_att = ''
rush_yard = ''
rush_td = ''
targets = ''
rec = ''
rec_yard = ''
rec_td = ''
fg_made = ''
fg_att = ''
fg_percent = ''
xp_made = ''
xp_att = ''
sack = ''
fumble_rec = ''
interception = ''
def_td = ''
pts_agst = ''
pass_agst = ''
rush_agst = ''
safety = ''
kick_td = ''
pts_wk = ''
pts_season = ''
sql = ''
final_sql = ''
i = 0

# following code is ran based on the user input for position
if position == '10':
    # loops through beautiful soup information and assigns information to variables
    while i < len(statistics):
        q = statistics[i].get_text()
        line = q.split(' ')
        rank = line[0]
        rank = rank[:-1]
        fName = line[1]
        lName = line[2]
        i += 1
        team = statistics[i].get_text()
        i += 1
        gp = statistics[i].get_text()
        i += 1
        comp = statistics[i].get_text()
        i += 1
        pass_att = statistics[i].get_text()
        i += 1
        pass_yard = statistics[i].get_text()
        pass_yard = pass_yard.replace(",", "")
        i += 1
        pass_td = statistics[i].get_text()
        i += 1
        inter = statistics[i].get_text()
        i += 1
        rush_att = statistics[i].get_text()
        i += 1
        rush_yard = statistics[i].get_text()
        rush_yard = rush_yard.replace(",", "")
        i += 1
        rush_td = statistics[i].get_text()
        i += 1
        pts_season = statistics[i].get_text()
        i += 1
        pts_wk = statistics[i].get_text()
        i += 1

        # format to enter into SQL
        if week == "Season":
            sql = ("(" + rank + ", '" + fName + "', '" + lName + "', '" + team + "', " + gp + ", " + comp + ", " +
                   pass_att + ", " + pass_yard + ", " + pass_td + ", " + inter + ", " + rush_att + ", " + rush_yard +
                   ", " + rush_td + ", " + pts_season + ", " + pts_wk + "),")
        elif week != "Season":
            sql = ("(" + rank + ", '" + fName + "', '" + lName + "', '" + team + "', " + comp + ", " + pass_att + ", "
                   + pass_yard + ", " + pass_td + ", " + inter + ", " + rush_att + ", " + rush_yard + "," + rush_td
                   + ", " + pts_wk + "),")

        if len(final_sql) == 0:
            final_sql = sql
        else:
            final_sql = (final_sql + '\n'
                         + sql)


elif position == '20':
    while i < len(statistics):
        q = statistics[i].get_text()
        line = q.split(' ')
        rank = line[0]
        rank = rank[:-1]
        fName = line[1]
        lName = line[2]
        i += 1
        team = statistics[i].get_text()
        i += 1
        gp = statistics[i].get_text()
        i += 1
        rush_att = statistics[i].get_text()
        i += 1
        rush_yard = statistics[i].get_text()
        rush_yard = rush_yard.replace(",", "")
        i += 1
        rush_td = statistics[i].get_text()
        i += 1
        targets = statistics[i].get_text()
        i += 1
        rec = statistics[i].get_text()
        i += 1
        rec_yard = statistics[i].get_text()
        rec_yard = rec_yard.replace(",", "")
        i += 1
        rec_td = statistics[i].get_text()
        i += 1
        pts_season = statistics[i].get_text()
        i += 1
        pts_wk = statistics[i].get_text()
        i += 1

        if week == "Season":
            sql = ("(" + rank + ", '" + fName + "', '" + lName + "', '" + team + "', " + gp + ", " + rush_att + ", " +
                   rush_yard + ", " + rush_td + ", " + targets + ", " + rec + ", " + rec_yard + ", " + rec_td + ", " +
                   pts_season + ", " + pts_wk + "),")
        elif week != "Season":
            sql = ("(" + rank + ", '" + fName + "', '" + lName + "', '" + team + "', " + rush_att + ", " + rush_yard +
                   ", " + rush_td + ", " + targets + ", " + rec + ", " + rec_yard + ", " + rec_td + ", " + pts_wk +
                   "),")

        if len(final_sql) == 0:
            final_sql = sql
        else:
            final_sql = (final_sql + '\n'
                         + sql)

elif position == '30':
    while i < len(statistics):
        q = statistics[i].get_text()
        line = q.split(' ')
        rank = line[0]
        rank = rank[:-1]
        fName = line[1]
        lName = line[2]
        i += 1
        team = statistics[i].get_text()
        i += 1
        gp = statistics[i].get_text()
        i += 1
        targets = statistics[i].get_text()
        i += 1
        rec = statistics[i].get_text()
        i += 1
        rec_yard = statistics[i].get_text()
        rec_yard = rec_yard.replace(",", "")
        i += 1
        rec_td = statistics[i].get_text()
        i += 1
        rush_att = statistics[i].get_text()
        i += 1
        rush_yard = statistics[i].get_text()
        rush_yard = rush_yard.replace(",", "")
        i += 1
        rush_td = statistics[i].get_text()
        i += 1
        pts_season = statistics[i].get_text()
        i += 1
        pts_wk = statistics[i].get_text()
        i += 1

        if week == "Season":
            sql = ("(" + rank + ", '" + fName + "', '" + lName + "', '" + team + "', " + gp + ", " + targets + ", " +
                   rec + ", " + rec_yard + ", " + rec_td + ", " + rush_att + ", " + rush_yard + ", " + rush_td + "," +
                   pts_season + ", " + pts_wk + "),")
        elif week != "Season":
            sql = ("(" + rank + ", '" + fName + "', '" + lName + "', '" + team + "', " + targets + ", " + rec + ", " +
                   rec_yard + ", " + rec_td + ", " + rush_att + ", " + rush_yard + ", " + rush_td + ", " + pts_wk + "),")

        if len(final_sql) == 0:
            final_sql = sql
        else:
            final_sql = (final_sql + '\n'
                         + sql)

elif position == '40':
    while i < len(statistics):
        q = statistics[i].get_text()
        line = q.split(' ')
        rank = line[0]
        rank = rank[:-1]
        fName = line[1]
        lName = line[2]
        i += 1
        team = statistics[i].get_text()
        i += 1
        gp = statistics[i].get_text()
        i += 1
        targets = statistics[i].get_text()
        i += 1
        rec = statistics[i].get_text()
        i += 1
        rec_yard = statistics[i].get_text()
        rec_yard = rec_yard.replace(",", "")
        i += 1
        rec_td = statistics[i].get_text()
        i += 1
        pts_season = statistics[i].get_text()
        i += 1
        pts_wk = statistics[i].get_text()
        i += 1

        if week == "Season":
            sql = ("(" + rank + ", '" + fName + "', '" + lName + "', '" + team + "', " + gp + ", " + targets + ", " +
                   rec + ", " + rec_yard + ", " + rec_td + ", " + pts_season + ", " + pts_wk + "),")
        elif week != "Season":
            sql = ("(" + rank + ", '" + fName + "', '" + lName + "', '" + team + "', " + targets + ", " + rec + ", " +
                   rec_yard + ", " + rec_td + ", " + pts_wk + "),")

        if len(final_sql) == 0:
            final_sql = sql
        else:
            final_sql = (final_sql + '\n'
                         + sql)

elif position == '80':
    while i < len(statistics):
        q = statistics[i].get_text()
        line = q.split(' ')
        rank = line[0]
        rank = rank[:-1]
        fName = line[1]
        lName = line[2]
        i += 1
        team = statistics[i].get_text()
        i += 1
        gp = statistics[i].get_text()
        i += 1
        fg_made = statistics[i].get_text()
        i += 1
        fg_att = statistics[i].get_text()
        i += 1
        fg_percent = statistics[i].get_text()[:-1]
        i += 1
        xp_made = statistics[i].get_text()
        i += 1
        xp_att = statistics[i].get_text()
        i += 1
        pts_season = statistics[i].get_text()
        i += 1
        pts_wk = statistics[i].get_text()
        i += 1

        if week == "Season":
            sql = ("(" + rank + ", '" + fName + "', '" + lName + "', '" + team + "', " + gp + ", " + fg_made + ", " +
                   fg_att + ", " + fg_percent + ", " + xp_made + ", " + xp_att + ", " + pts_season + ", " + pts_wk +
                   "),")
        elif week != "Season":
            sql = ("(" + rank + ", '" + fName + "', '" + lName + "', '" + team + "', " + fg_made + ", " + fg_att +
                   ", " + fg_percent + ", " + xp_made + ", " + xp_att + ", " + pts_wk + "),")

        if len(final_sql) == 0:
            final_sql = sql
        else:
            final_sql = (final_sql + '\n'
                         + sql)

elif position == '99':
    while i < len(statistics):
        q = statistics[i].get_text()
        line = q.split(' ')
        rank = line[0]
        rank = rank[:-1]
        if len(line) > 3:
            fName = line[1] + ' ' + line[2]
            lName = line[3]
        else:
            fName = line[1]
            lName = line[2]
        i += 2
        sack = statistics[i].get_text()
        i += 1
        fumble_rec = statistics[i].get_text()
        i += 1
        interception = statistics[i].get_text()
        i += 1
        def_td = statistics[i].get_text()
        i += 1
        pts_agst = statistics[i].get_text()
        i += 1
        pass_agst = statistics[i].get_text()
        i += 1
        rush_agst = statistics[i].get_text()
        i += 1
        safety = statistics[i].get_text()
        i += 1
        kick_td = statistics[i].get_text()
        i += 1
        pts_season = statistics[i].get_text()
        i += 1
        pts_wk = statistics[i].get_text()
        i += 1

        if week == "Season":
            sql = ("(" + rank + ", '" + fName + "', '" + lName + "', " + sack + ", " + fumble_rec + ", " +
                   interception + ", " + def_td + ", " + pts_agst + ", " + pass_agst + ", " + rush_agst + ", " + safety
                   + ", " + kick_td + ", " + pts_season + ", " + pts_wk + "),")
        elif week != "Season":
            sql = ("(" + rank + ", '" + fName + "', '" + lName + "', " + sack + ", " + fumble_rec + ", " +
                   interception + ", " + def_td + ", " + pts_agst + ", " + pass_agst + ", " + rush_agst + ", " + safety
                   + ", " + kick_td + ", " + pts_wk + "),")

        if len(final_sql) == 0:
            final_sql = sql
        else:
            final_sql = (final_sql + '\n'
                         + sql)

pyperclip.copy(final_sql)

