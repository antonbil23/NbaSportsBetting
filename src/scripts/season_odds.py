import datetime
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException

# We will be using code from https://colab.research.google.com/drive/1STvYH8iwru1xHe3uT1oUPjwPN8Qgv7mP?authuser=1#scrollTo=5vYU1bQQIid1
# for the gathering 2024 season odds
import time


month = {
    "January": 1,
    "February": 2,
    "March": 3,
    "April": 4,
    "May": 5,
    "June": 6,
    "July": 7,
    "August": 8,
    "September": 9,
    "October": 10,
    "November": 11,
    "December": 12
}

referenceTable = {
    "NY" : "NYK",
    "UTAH" : "UTA",
    "NO" : "NOP",
    "SA" : "SAS",
    "GS" : "GSW",
    "WSH" : "WAS"
}

# Define retry function
def get_with_retry(driver, url, max_retries=8, delay=10):
    retries = 0
    while retries < max_retries:
        try:
            driver.get(url)
            return driver.page_source
        except TimeoutException as e:
            print(f"Timeout error occurred: {e}. Retrying...")
        except Exception as e:
            print(f"An error occurred: {e}. Retrying...")
        
        retries += 1
        time.sleep(delay)  # Wait for a short delay before retrying
    
    print("Max retries reached. Unable to fetch data.")
    return None

def getGames():
    games = []
    checker = False

    # gameid ranges for the 2024 nba season
    # 401584689 (start gameid)
    #401585704+1 (3-30-2024 gamid)
    # 401585825 (end gameid)
    for i in range (401584689, 401585825+1):


        url= "https://www.espn.com/nba/boxscore/_/gameId/" + str(i)

        # chrome_options = Options()
        options = webdriver.ChromeOptions()
        options.add_argument("--window-size=1920,1080")
        options.add_argument("--headless")
        options.add_argument("--disable-gpu")
        options.add_argument(
            "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36")
        driver = webdriver.Chrome(executable_path='C:/Drivers/chromedriver.exe', options=options)

        content = get_with_retry(driver, url)
        if content is None:
            continue

        content = content.encode('utf-8').strip()
        soup = BeautifulSoup(content,"html.parser")

        g = getOdds(soup)

        # this will print out the gameId ranges idk why but it does
        if g != None:
            if not checker:
                print('[', i)
            games.append(g)
            checker = True
        elif checker:
            print(i - 1, ']')
            checker = False
        driver.quit()

    return games


def getOdds(soup):
    results = soup.find(class_="n8 GameInfo__Meta")
    # Return none if page is empty
    if results is None:
        return None
    # Gets date of game
    date_list = results.text.split(" ")
    date = datetime.datetime(int(date_list[4][:4]), int(month[date_list[2]]), int(date_list[3][:-1]))
    date_string = date.strftime("%Y-%m-%d")

    # Gets name of teams that played
    results = soup.find_all(class_="ScoreCell__Truncate Gamestrip__Truncate h4 clr-gray-01")
    away = results[0].find('a', href=True)['href'].split("/")[-2].upper()
    home = results[1].find('a', href=True)['href'].split("/")[-2].upper()

    # Changes team initials if needed for conversion
    a = referenceTable.get(away)
    if a is None:
        a = away
    h = referenceTable.get(home)
    if h is None:
        h = home

    results = soup.find(class_="betting-details-with-logo")
    # Return none if game was not played
    if results is not None:
        odds = results.find_all('div')
        line = odds[0].text.split(' ')
        overunder = odds[1].text.split(' ')
    else:
        return None

    # Gets line for game, 0 point spread if even
    if len(line) < 3:
        l = [home, "0"]
    else:
        l = line[1:]

    # Gets favorite of game
    fav = referenceTable.get(l[0])
    if fav is None:
        fav = l[0]

    line_string = fav + " " + l[1]

    # Formats overunder
    if float(overunder[1]) % 1 == 0:
        o = int(overunder[1])
    else:
        o = float(overunder[1])

    return ([date_string, a, h, fav, l[1], o])



def getOddsToCsv():
    games = getGames()
    games_lines_df = pd.DataFrame(games)
    games_lines_df = games_lines_df.rename(columns={0: 'Date', 1: 'Away', 2: 'Home', 3: 'Favorite', 4: 'Line', 5: 'Over/Under'})
    games_lines_df.to_csv('2024_Final_Season_Odds.csv')

getOddsToCsv()