import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Load the datasets
reputation_sentiment_daily = pd.read_csv('daily_sum_metrics_mean.csv')
btc_data = pd.read_csv('BTC-USD.csv')

# Step 2: Convert the 'time' column to datetime and set it as the index
reputation_sentiment_daily['time'] = pd.to_datetime(reputation_sentiment_daily['time']).dt.date
reputation_sentiment_daily.set_index('time', inplace=True)

# Convert the 'Date' column in 'btc_data' to datetime and set it as the index
btc_data['Date'] = pd.to_datetime(btc_data['Date'])
btc_data.set_index('Date', inplace=True)

# Step 3: Filter the data to include only dates from 2021-07-01 to 2021-12-31
start_date = '2021-06-01'
end_date = '2022-12-31'
reputation_sentiment_daily = reputation_sentiment_daily.loc[pd.to_datetime(start_date):pd.to_datetime(end_date)]
btc_data = btc_data.loc[pd.to_datetime(start_date):pd.to_datetime(end_date)]

# Step 4: Calculate BTC price change and BTC trade volume change
btc_data['BTC_Price_Change'] = btc_data['Close'].diff()
btc_data['BTC_Volume'] = btc_data['Volume'].diff()

# Step 5: Add lagged columns for BTC price change and BTC trade volume change (+1 day lag)
btc_data['BTC_Price_Change_Lagged'] = btc_data['BTC_Price_Change'].shift(-1)
btc_data['BTC_Volume_Lagged'] = btc_data['Volume'].shift(-1)

# Step 6: Merge the 'reputation_sentiment_daily' and 'btc_data' datasets
merged_data = reputation_sentiment_daily.merge(btc_data[['BTC_Price_Change', 'BTC_Price_Change_Lagged', 'BTC_Volume', 'BTC_Volume_Lagged']],
                                               left_index=True, right_index=True, how='inner')

# List of sentiment metrics
sentiment_metrics = ['sen', 'pos', 'neg', 'con', 'wordcnt', 'itemcnt','catastrophizing', 'dichotoreasoning', 'disqualpositive',
                     'emotionreasoning', 'fortunetelling', 'labeling', 'magnification',
                     'mentalfiltering', 'mindreading', 'overgeneralizing', 'personalizing',
                     'shouldment', 'exclusivereasoning', 'negativereasoning', 'mentalfilteringplus']

reputation_sentiment_metrics = ['Reputation_' + metric for metric in sentiment_metrics]

# Step 7: Create plots and calculate correlations
for metric in ['BTC_Price_Change', 'BTC_Volume'] + sentiment_metrics + reputation_sentiment_metrics:
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 12), sharex=True)

    # Metric vs BTC_Price_Change
    ax1.plot(merged_data.index, merged_data[metric], label=metric, color='blue')
    ax1.set_ylabel(metric, color='blue')
    ax1.tick_params(axis='y', labelcolor='blue')
    ax1.grid(True)

    # Secondary y-axis for BTC_Price_Change
    ax1_2 = ax1.twinx()
    ax1_2.plot(merged_data.index, merged_data['BTC_Price_Change'], label='BTC Price Change', color='orange', linestyle='dotted')
    ax1_2.set_ylabel('BTC Price Change', color='orange')
    ax1_2.tick_params(axis='y', labelcolor='orange')

    # Metric vs BTC_Volume
    ax2.plot(merged_data.index, merged_data[metric], label=metric, color='blue')
    ax2.set_xlabel('Date')
    ax2.set_ylabel(metric, color='blue')
    ax2.tick_params(axis='y', labelcolor='blue')
    ax2.grid(True)

    # Secondary y-axis for BTC_Volume
    ax2_2 = ax2.twinx()
    ax2_2.plot(merged_data.index, merged_data['BTC_Volume'], label='BTC Volume', color='green', linestyle='dotted')
    ax2_2.set_ylabel('BTC Volume', color='green')
    ax2_2.tick_params(axis='y', labelcolor='green')

    fig.suptitle(f'{metric} vs BTC Price Change and Volume')
    fig.legend(loc="upper right")
    plt.grid(True)

    # Calculate Pearson correlation
    correlation_metric_price = merged_data[metric].corr(merged_data['BTC_Price_Change'])
    correlation_metric_volume = merged_data[metric].corr(merged_data['BTC_Volume'])

    print(f"Pearson Correlation - {metric} vs BTC Price Change: {correlation_metric_price}")
    print(f"Pearson Correlation - {metric} vs BTC Volume: {correlation_metric_volume}")

# Calculate Pearson correlation for sentiment metrics vs BTC Price Change and Volume
correlation_results = []

for metric in sentiment_metrics + reputation_sentiment_metrics:
    correlation_metric_price = merged_data[metric].corr(merged_data['BTC_Price_Change'])
    correlation_metric_volume = merged_data[metric].corr(merged_data['BTC_Volume'])

    correlation_results.append({
        'Metric': metric,
        'Correlation with BTC Price Change': correlation_metric_price,
        'Correlation with BTC Volume': correlation_metric_volume
    })

# Create a DataFrame to store correlation values
correlation_df = pd.DataFrame(correlation_results)

# Step 13: Plot Pearson correlation scores
plt.figure(figsize=(12, 6))
plt.bar(correlation_df['Metric'], correlation_df['Correlation with BTC Price Change'], color='blue', label='BTC Price Change')
plt.bar(correlation_df['Metric'], correlation_df['Correlation with BTC Volume'], color='orange', label='BTC Volume')
plt.xticks(rotation=90)
plt.xlabel('Metrics')
plt.ylabel('Pearson Correlation')
plt.title('Pearson Correlation Scores')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

#
# # Step 7: Create plots and calculate correlations
# for metric in ['BTC_Price_Change_Lagged', 'BTC_Volume_Lagged'] + sentiment_metrics + reputation_sentiment_metrics:
#     fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 12), sharex=True)
#
#     # Metric vs BTC_Price_Change
#     ax1.plot(merged_data.index, merged_data[metric], label=metric, color='blue')
#     ax1.set_ylabel(metric, color='blue')
#     ax1.tick_params(axis='y', labelcolor='blue')
#     ax1.grid(True)
#
#     # Secondary y-axis for BTC_Price_Change
#     ax1_2 = ax1.twinx()
#     ax1_2.plot(merged_data.index, merged_data['BTC_Price_Change_Lagged'], label='BTC Price Change Lagged', color='orange', linestyle='dotted')
#     ax1_2.set_ylabel('BTC Price Change Lagged', color='orange')
#     ax1_2.tick_params(axis='y', labelcolor='orange')
#
#     # Metric vs BTC_Volume
#     ax2.plot(merged_data.index, merged_data[metric], label=metric, color='blue')
#     ax2.set_xlabel('Date')
#     ax2.set_ylabel(metric, color='blue')
#     ax2.tick_params(axis='y', labelcolor='blue')
#     ax2.grid(True)
#
#     # Secondary y-axis for BTC_Volume
#     ax2_2 = ax2.twinx()
#     ax2_2.plot(merged_data.index, merged_data['BTC_Volume_Lagged'], label='BTC Volume Lagged', color='green', linestyle='dotted')
#     ax2_2.set_ylabel('BTC Volume Lagged', color='green')
#     ax2_2.tick_params(axis='y', labelcolor='green')
#
#     fig.suptitle(f'{metric} vs BTC Price Change Lagged and Volume Lagged')
#     fig.legend(loc="upper right")
#     plt.grid(True)
#
#     # Calculate Pearson correlation
#     correlation_metric_price = merged_data[metric].corr(merged_data['BTC_Price_Change_Lagged'])
#     correlation_metric_volume = merged_data[metric].corr(merged_data['BTC_Volume_Lagged'])
#
#     print(f"Pearson Correlation - {metric} vs BTC Price Change Lagged: {correlation_metric_price}")
#     print(f"Pearson Correlation - {metric} vs BTC Volume Lagged: {correlation_metric_volume}")
#
# # Step 12: Create a DataFrame to store correlation values
#
# # Define reputation sentiment metrics
# reputation_sentiment_metrics = ['Reputation_' + metric for metric in sentiment_metrics]
#
# # Calculate Pearson correlation for sentiment metrics vs Lagged BTC Price Change and Volume
# correlation_results_lagged = []
#
# for metric in sentiment_metrics + reputation_sentiment_metrics:
#     correlation_metric_price_lagged = merged_data[metric].corr(merged_data['BTC_Price_Change_Lagged'])
#     correlation_metric_volume_lagged = merged_data[metric].corr(merged_data['BTC_Volume_Lagged'])
#
#     correlation_results_lagged.append({
#         'Metric': metric,
#         'Correlation with BTC Price Change Lagged': correlation_metric_price_lagged,
#         'Correlation with BTC Volume Lagged': correlation_metric_volume_lagged
#     })
#
# # Create a DataFrame to store lagged correlation values
# correlation_df_lagged = pd.DataFrame(correlation_results_lagged)
#
# # # Plot Pearson correlation scores for lagged data
# plt.figure(figsize=(12, 6))
# plt.bar(correlation_df_lagged['Metric'], correlation_df_lagged['Correlation with BTC Price Change Lagged'], color='blue', label='BTC Price Change Lagged')
# plt.bar(correlation_df_lagged['Metric'], correlation_df_lagged['Correlation with BTC Volume Lagged'], color='orange', label='BTC Volume Lagged')
# plt.xticks(rotation=90)
# plt.xlabel('Metrics')
# plt.ylabel('Pearson Correlation')
# plt.title('Pearson Correlation Scores for Lagged Data')
# plt.legend()
# plt.grid(True)
# plt.tight_layout()
# plt.show()