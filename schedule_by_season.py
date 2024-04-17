import sys
import pandas as pd
from basketball_reference_scraper.seasons import get_schedule
from basketball_reference_scraper.box_scores import get_box_scores
import warnings
# from io import StringIO
warnings.filterwarnings("ignore", category=FutureWarning, message="Passing literal html to 'read_html' is deprecated")

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
# get_schedule(year, playoffs=False).to_csv(f"schedule_{year}.csv", sep=',', index=False, encoding='utf-8')

def create_game_files(year):
    df = pd.read_csv(f"schedule_{year}.csv")
    total_df = pd.DataFrame()
    for index, row in df.iterrows():
        if row["VISITOR_PTS"] == "":
            continue

        combined_df = pd.DataFrame()
        date = row['DATE']
        away = team_abbreviations[row['VISITOR'].upper()]
        home = team_abbreviations[row['HOME'].upper()]
        print(home)
        d = get_box_scores(date, away, home)
        # d[away].to_csv(f"{away}_{date}.csv", sep=',', index=False, encoding='utf-8')
        # d[home].to_csv(f"{home}_{date}.csv", sep=',', index=False, encoding='utf-8')
        df_away = d[away]
        df_home = d[home]

        df_away = df_away[df_away['PLAYER'] == 'Team Totals']
        df_home = df_home[df_home['PLAYER'] == 'Team Totals']

        df_away = df_away.rename(columns={'PLAYER': "TEAM"})
        df_home = df_home.rename(columns={'PLAYER': "TEAM"})

        df_away["TEAM"] = away
        df_home["TEAM"] = home

        away_opp = df_away.copy(deep=True)
        away_opp = away_opp.add_suffix("_opp")
        away_opp.insert(len(away_opp.columns), 'date', date)
        away_opp.insert(len(away_opp.columns), 'won', 0 if row['VISITOR_PTS'] > row['HOME_PTS'] else 1)

        home_opp = df_home.copy(deep=True)
        home_opp = home_opp.add_suffix("_opp")
        home_opp.insert(len(home_opp.columns), 'date', date)
        home_opp.insert(len(home_opp.columns), 'won', 1 if row['VISITOR_PTS'] > row['HOME_PTS'] else 0)
        # if isinstance(home_opp, pd.DataFrame):
        #     print("home is a dataframe")
        
        combined_df = pd.concat([combined_df, df_away, home_opp], ignore_index=True)
        combined_row = combined_df.iloc[0].combine_first(combined_df.iloc[1])
        combined_df.loc[0] = combined_row
        combined_df = combined_df.drop(1)

        combined_df = pd.concat([combined_df, df_home, away_opp], ignore_index=True)
        combined_row = combined_df.iloc[1].combine_first(combined_df.iloc[2])
        combined_df.loc[1] = combined_row
        combined_df = combined_df.drop(2)

        # combined_df.to_csv(f"combined_{year}.csv", sep=',', index=False, encoding='utf-8')
        total_df = pd.concat([total_df, combined_df], ignore_index=True)
    total_df.to_csv(f"combined_{year}.csv", sep=',', index=False, encoding='utf-8')

create_game_files(year)