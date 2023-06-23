import pandas as pd

# Read the dataset into a pandas DataFrame, specifying the 'date' column as a string
df = pd.read_csv('sentiment_scores.csv', dtype={'date': str})

# Select the desired columns
selected_columns = ['user_name', 'date', 'sentiment_score']
df_selected = df[selected_columns]

# Convert the 'date' column to datetime format
df_selected['date'] = pd.to_datetime(df_selected['date'], errors='coerce')

# Set the 'date' column as the index
df_selected.set_index('date', inplace=True)

# Check if the 'date' column is in datetime format
is_datetime = pd.api.types.is_datetime64_any_dtype(df_selected.index)

# Save the resulting DataFrame to a CSV file
df_selected.to_csv('selected_data.csv')

# Print the resulting DataFrame and the datetime format check
print(df_selected)
print("Is 'date' column in datetime format?", is_datetime)
