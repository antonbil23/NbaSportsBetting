import pandas as pd

# Read the CSV file
df = pd.read_csv('/Users/rahul/Documents/Development/NbaSportsBetting/data/season-data/combined_2024.csv')

# Convert column names to lowercase
df.columns = df.columns.str.lower()

# Save the modified DataFrame back to the CSV file
df.to_csv('/Users/rahul/Documents/Development/NbaSportsBetting/data/season-data/combined_2024.csv', index=False)
