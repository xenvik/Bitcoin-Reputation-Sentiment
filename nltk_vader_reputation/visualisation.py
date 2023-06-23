import pandas as pd
import matplotlib.pyplot as plt

# Read the merged_data.csv file into a DataFrame
df_merged = pd.read_csv('merged_data.csv')

# Set the 'date' column as the index and convert it to datetime
df_merged['date'] = pd.to_datetime(df_merged['date'])
df_merged.set_index('date', inplace=True)

# Resample the DataFrame on a daily basis and sum the 'sentiment_score' and 'reputation_sentiment'
df_daily = df_merged.resample('D').sum()

# Remove the 'user_name' and 'reputation' columns
df_daily.drop(['user_name', 'reputation'], axis=1, inplace=True)

# Interpolate zero sentiment scores
df_daily['sentiment_score'] = df_daily['sentiment_score'].replace(0, pd.NA).interpolate(method='linear')

# Replace NA values with the average sentiment score
avg_sentiment_score = df_daily['sentiment_score'].mean()
df_daily['sentiment_score'].fillna(avg_sentiment_score, inplace=True)

# Read the BTCUSD_1h.csv file into a DataFrame
df_btc = pd.read_csv('BTCUSD_1h.csv')

# Set the 'date' column as the index and convert it to datetime
df_btc['date'] = pd.to_datetime(df_btc['date'])
df_btc.set_index('date', inplace=True)

# Merge the processed DataFrame with the BTCUSD DataFrame based on the daily dates
df_final = pd.merge(df_daily, df_btc['close'], left_index=True, right_index=True)

# Save the final processed dataframe to a CSV file
df_final.to_csv('final_data.csv')

# Plot BTC daily close price with sentiments and reputation_sentiments
fig, ax1 = plt.subplots()

# Plot BTC close price
ax1.plot(df_final.index, df_final['close'], color='b')
ax1.set_xlabel('Date')
ax1.set_ylabel('BTC Close Price', color='b')
ax1.tick_params('y', colors='b')

# Create a secondary y-axis for sentiment scores
ax2 = ax1.twinx()

# Plot sentiment scores
ax2.plot(df_final.index, df_final['sentiment_score'].astype(float), color='r', linestyle='--', label='Sentiment Score')
ax2.plot(df_final.index, df_final['reputation_sentiment'].astype(float), color='g', linestyle='--', label='Reputation Sentiment')
ax2.set_ylabel('Sentiment Scores', color='r')
ax2.tick_params('y', colors='r')

# Set the legend
lines = ax1.get_lines() + ax2.get_lines()
ax1.legend(lines, [line.get_label() for line in lines], loc='upper left')

# Show the plot
plt.savefig('figure.png')