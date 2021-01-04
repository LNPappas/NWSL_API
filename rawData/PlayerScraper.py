import requests
from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Chrome()
# url = "https://fbref.com/en/comps/182/2940/stats/2013-NWSL-Stats"
# url = "https://fbref.com/en/comps/182/2941/stats/2014-NWSL-Stats"
# url = "https://fbref.com/en/comps/182/2942/stats/2015-NWSL-Stats"
# url = "https://fbref.com/en/comps/182/2943/stats/2016-NWSL-Stats"
# url = "https://fbref.com/en/comps/182/2944/stats/2017-NWSL-Stats"
# url = "https://fbref.com/en/comps/182/2945/stats/2018-NWSL-Stats"
url = "https://fbref.com/en/comps/182/2946/stats/2019-NWSL-Stats"
# url = ""
driver.get(url)
soup = BeautifulSoup(driver.page_source, "lxml")
players = [["First", "Last", "Country", "Pos", "Team", "Age", "DOB", "MP", "Starts", "Min", "Gls", "Ast", "PK", "PKatt", "CrdY", "CrdR", "Gls90", "Ast90", "G+A90", "G-PK90", "G+A-PK90", "Number", "Hometown", "Height"]]

table = soup.select("#stats_standard")
for items in table[0].select("tr"):
    for ele in items.select("td"):
        player = items.select("[data-stat='player']")[0].text
        nation = items.select("[data-stat='nationality']")[0].text
        position = items.select("[data-stat='position']")[0].text
        squad = items.select("[data-stat='squad']")[0].text
        age = items.select("[data-stat='age']")[0].text
        dob = items.select("[data-stat='birth_year']")[0].text
        games = items.select("[data-stat='games']")[0].text
        game_start = items.select("[data-stat='games_starts']")[0].text
        minutes = items.select("[data-stat='minutes']")[0].text
        goals = items.select("[data-stat='goals']")[0].text
        assists = items.select("[data-stat='assists']")[0].text
        pk = items.select("[data-stat='pens_made']")[0].text
        pkattempt = items.select("[data-stat='pens_att']")[0].text
        yc = items.select("[data-stat='cards_yellow']")[0].text
        rc = items.select("[data-stat='cards_red']")[0].text
        goal90 = items.select("[data-stat='goals_per90']")[0].text
        assists90 = items.select("[data-stat='assists_per90']")[0].text
        ga90 = items.select("[data-stat='goals_assists_per90']")[0].text
        pk90 = items.select("[data-stat='goals_pens_per90']")[0].text
        gapk90 =  items.select("[data-stat='goals_assists_pens_per90']")[0].text
        all = [player, nation[3:], position, squad, age, dob, games, game_start, minutes, goals, assists, pk, pkattempt, yc, rc, goal90, assists90, ga90, pk90, gapk90, "-", "-", "-"]
        for i,v in enumerate(all):
            if v == '':
                all[i] = '-'
        players.append(all)
        break

driver.quit()

file2 = open('temp.txt', 'w')
for p in players:
    try:
        s = ' '.join(p) + '\n'
        file2.writelines(s)
    except: 
        print(p)

file2.close()
