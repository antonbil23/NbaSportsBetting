import pandas as pd

# Read the CSV file
df = pd.read_csv("combined_2024.csv")

# Remove the columns "+/-" and "+/-_opp"
df = df.drop(["+/-", "+/-_opp"], axis=1)

# Print the updated DataFrame
df.to_csv("combined_2024_temp.csv", index=False)