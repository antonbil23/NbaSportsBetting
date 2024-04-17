import sys
import pandas as pd
from basketball_reference_scraper.seasons import get_schedule
from basketball_reference_scraper.box_scores import get_box_scores

team_abbreviations = {
    "ATLANTA HAWKS": "ATL",
    "ST. LOUIS HAWKS": "SLH",
    "MILWAUKEE HAWKS": "MIL",
    "TRI-CITIES BLACKHAWKS": "TCB",
    "BOSTON CELTICS": "BOS",
    "BROOKLYN NETS": "BRK",
    "NEW JERSEY NETS": "NJN",
    "CHICAGO BULLS": "CHI",
    "CHARLOTTE HORNETS (1988-2004)": "CHH",
    "CHARLOTTE HORNETS": "CHO",
    "CHARLOTTE BOBCATS": "CHA",
    "CLEVELAND CAVALIERS": "CLE",
    "DALLAS MAVERICKS": "DAL",
    "DENVER NUGGETS": "DEN",
    "DETROIT PISTONS": "DET",
    "FORT WAYNE PISTONS": "FWP",
    "GOLDEN STATE WARRIORS": "GSW",
    "SAN FRANCISCO WARRIORS": "SFW",
    "PHILADELPHIA WARRIORS": "PHI",
    "HOUSTON ROCKETS": "HOU",
    "INDIANA PACERS": "IND",
    "LOS ANGELES CLIPPERS": "LAC",
    "SAN DIEGO CLIPPERS": "SDC",
    "BUFFALO BRAVES": "BUF",
    "LOS ANGELES LAKERS": "LAL",
    "MINNEAPOLIS LAKERS": "MIN",
    "MEMPHIS GRIZZLIES": "MEM",
    "VANCOUVER GRIZZLIES": "VAN",
    "MIAMI HEAT": "MIA",
    "MILWAUKEE BUCKS": "MIL",
    "MINNESOTA TIMBERWOLVES": "MIN",
    "NEW ORLEANS PELICANS": "NOP",
    "NEW ORLEANS/OKLAHOMA CITY HORNETS": "NOK",
    "NEW ORLEANS HORNETS": "NOH",
    "NEW YORK KNICKS": "NYK",
    "OKLAHOMA CITY THUNDER": "OKC",
    "SEATTLE SUPERSONICS": "SEA",
    "ORLANDO MAGIC": "ORL",
    "PHILADELPHIA 76ERS": "PHI",
    "SYRACUSE NATIONALS": "SYR",
    "PHOENIX SUNS": "PHO",
    "PORTLAND TRAIL BLAZERS": "POR",
    "SACRAMENTO KINGS": "SAC",
    "KANSAS CITY KINGS": "KCK",
    "KANSAS CITY-OMAHA KINGS": "KCK",
    "CINCINNATI ROYALS": "CIN",
    "ROCHESTER ROYALS": "ROR",
    "SAN ANTONIO SPURS": "SAS",
    "TORONTO RAPTORS": "TOR",
    "UTAH JAZZ": "UTA",
    "NEW ORLEANS JAZZ": "NOJ",
    "WASHINGTON WIZARDS": "WAS",
    "WASHINGTON BULLETS": "WAS",
    "CAPITAL BULLETS": "CAP",
    "BALTIMORE BULLETS": "BAL",
    "CHICAGO ZEPHYRS": "CHI",
    "CHICAGO PACKERS": "CHI",
    "ANDERSON PACKERS": "AND",
    "CHICAGO STAGS": "CHI",
    "INDIANAPOLIS OLYMPIANS": "IND",
    "SHEBOYGAN RED SKINS": "SRS",
    "ST. LOUIS BOMBERS": "SLB",
    "WASHINGTON CAPITOLS": "WAS",
    "WATERLOO HAWKS": "WAT",
    "SAN DIEGO ROCKETS": "SDR"
}

year = int(sys.argv[1])
get_schedule(year, playoffs=False).to_csv(f"schedule_{year}.csv", sep=',', index=False, encoding='utf-8')

def create_game_files(year):
    df = pd.read_csv(f"schedule_{year}.csv")
    combined_df = pd.DataFrame()
    for index, row in df.iterrows():
        date = row['DATE']
        away = team_abbreviations[row['VISITOR'].upper()]
        home = team_abbreviations[row['HOME'].upper()]
        d = get_box_scores(date, away, home)
        d[away].to_csv(f"{away}_{date}.csv", sep=',', index=False, encoding='utf-8')
        d[home].to_csv(f"{home}_{date}.csv", sep=',', index=False, encoding='utf-8')
        #  TODO: format the data better, team totals are not in a good place
        combined_df = pd.concat([combined_df, d[away], d[home]], ignore_index=True)
        combined_df.to_csv(f"combined_{year}.csv", sep=',', index=False, encoding='utf-8')
        
        break

create_game_files(year)