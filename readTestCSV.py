import pandas as pd
# Read the CSV file
df = pd.read_csv('https://raw.githubusercontent.com/dcsteph7/Data-Capstone/main/nba_games1.csv', index_col=0)

# Print the headers
print(df.columns)
df = df.sort_values("date")
df = df.reset_index(drop=True)

# print(df.columns)
# print(len(df))
# Print the first 4 rows
df.head(4).to_csv('/Users/rahul/Documents/Development/NbaSportsBetting/first_4_rows.csv', index=False)
