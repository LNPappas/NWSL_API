import requests
from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Chrome()
url = "https://fbref.com/en/comps/182/2940/stats/2013-NWSL-Stats"
# url = "https://fbref.com/en/comps/182/2941/stats/2014-NWSL-Stats"
# url = "https://fbref.com/en/comps/182/2942/stats/2015-NWSL-Stats"
# url = "https://fbref.com/en/comps/182/2943/stats/2016-NWSL-Stats"
# url = "https://fbref.com/en/comps/182/2944/stats/2017-NWSL-Stats"
# url = "https://fbref.com/en/comps/182/2945/stats/2018-NWSL-Stats"
# url = "https://fbref.com/en/comps/182/2946/stats/2019-NWSL-Stats"
# url = ""
driver.get(url)
soup = BeautifulSoup(driver.page_source, "lxml")
table = soup.select("#stats_standard_squads")
teams = [['Team', "#Players", "#PlayersInGame", "MP", "Starts", "Min", "Goals", "Assists", "PK", "PKattempts", "YC", "RC", "Gls90", "Ast90", "G+A90", "G-PK90", "G+A-PK90"]]
for items in table[0].select("tr"):
    for ele in items.select("td"):
        print(items.select("[data-stat='squad']")[0].text)
        break

driver.quit()

file = open('temp.txt', 'w')
for t in teams:
    try:
        s = ' '.join(t) + '\n'
        file.writelines(s)
    except: 
        print(t)

file.close()