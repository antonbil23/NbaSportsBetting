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
# df.to_csv('/Users/rahul/Documents/Development/NbaSportsBetting/2012_to_2023_data.csv', index=False)

# Read the combined_2024.csv file
df_combined = pd.read_csv('./schedule/combined_2024.csv')

# Keep only the columns that match in both dataframes
df = df[df.columns.str.lower().intersection(df_combined.columns.str.lower())]

# Print the updated dataframe
df.to_csv('/Users/rahul/Documents/Development/NbaSportsBetting/2012_to_2023_data.csv', index=False)

df_combined.columns = df_combined.columns.str.lower()
combined_df = pd.concat([df, df_combined], ignore_index=True)

# Print the combined dataframe
combined_df.to_csv('/Users/rahul/Documents/Development/NbaSportsBetting/2012_to_2024_data.csv', index=False)
