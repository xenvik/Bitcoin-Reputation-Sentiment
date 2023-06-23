import pandas as pd

# Read the selected data and reputation scores into DataFrames
df_selected = pd.read_csv('selected_data.csv')
df_reputation = pd.read_csv('reputation_scores.csv')

# Merge the DataFrames based on the 'user_name' column
df_merged = pd.merge(df_selected, df_reputation, on='user_name')

# Normalize the 'reputation' column
max_reputation = df_merged['reputation'].max()
df_merged['reputation'] = df_merged['reputation'] / max_reputation

# Create a new column 'reputation_sentiment' as the product of 'reputation' and 'sentiment_score'
df_merged['reputation_sentiment'] = df_merged['reputation'] * df_merged['sentiment_score']

# Convert the 'date' column to datetime
df_merged['date'] = pd.to_datetime(df_merged['date'], errors='coerce')

# Remove rows without a valid date-time value
df_merged.dropna(subset=['date'], inplace=True)

# Sort the merged DataFrame based on the 'date' column from the selected_data.csv
df_merged.sort_values(by='date', inplace=True)

# Rearrange the columns to have 'date', 'user_name', 'sentiment_score', 'reputation', and 'reputation_sentiment'
df_merged = df_merged[['date', 'user_name', 'sentiment_score', 'reputation', 'reputation_sentiment']]

# Save the resulting DataFrame to a CSV file
df_merged.to_csv('merged_data.csv', index=False)

# Print the resulting DataFrame
print(df_merged)
