import pandas as pd

# Load the reputation sentiment data
data = pd.read_csv('reputation_all_updated.csv')

# Set the 'time' column as datetime
data['time'] = pd.to_datetime(data['time'])

# Group the data by date and calculate the sum of 'sen', 'Reputation_Score', and 'Reputation_Sentiment'
daily_metrics = data.groupby(data['time'].dt.date)[['sen', 'pos', 'neg', 'con','wordcnt', 'itemcnt', 'Reputation_wordcnt', 'Reputation_itemcnt', 'catastrophizing', 'dichotoreasoning', 'disqualpositive', 'emotionreasoning',
                                                'fortunetelling', 'labeling', 'magnification', 'mentalfiltering', 'mindreading', 'overgeneralizing',
                                                'personalizing', 'shouldment', 'exclusivereasoning', 'negativereasoning', 'mentalfilteringplus',
                                                'Reputation_Score', 'Reputation_sen', 'Reputation_pos', 'Reputation_neg', 'Reputation_con', 'Reputation_catastrophizing',
                                                'Reputation_dichotoreasoning', 'Reputation_disqualpositive', 'Reputation_emotionreasoning',
                                                'Reputation_fortunetelling', 'Reputation_labeling', 'Reputation_magnification', 'Reputation_mentalfiltering',
                                                'Reputation_mindreading', 'Reputation_overgeneralizing', 'Reputation_personalizing', 'Reputation_shouldment',
                                                'Reputation_exclusivereasoning', 'Reputation_negativereasoning', 'Reputation_mentalfilteringplus']].sum()

# daily_mean = data.groupby(data['time'].dt.date)[['sen', 'pos', 'neg', 'con', 'catastrophizing', 'dichotoreasoning', 'disqualpositive', 'emotionreasoning',
#                                                 'fortunetelling', 'labeling', 'magnification', 'mentalfiltering', 'mindreading', 'overgeneralizing',
#                                                 'personalizing', 'shouldment', 'exclusivereasoning', 'negativereasoning', 'mentalfilteringplus',
#                                                 'Reputation_Score', 'Reputation_sen', 'Reputation_pos', 'Reputation_neg', 'Reputation_con', 'Reputation_catastrophizing',
#                                                 'Reputation_dichotoreasoning', 'Reputation_disqualpositive', 'Reputation_emotionreasoning',
#                                                 'Reputation_fortunetelling', 'Reputation_labeling', 'Reputation_magnification', 'Reputation_mentalfiltering',
#                                                 'Reputation_mindreading', 'Reputation_overgeneralizing', 'Reputation_personalizing', 'Reputation_shouldment',
#                                                 'Reputation_exclusivereasoning', 'Reputation_negativereasoning', 'Reputation_mentalfilteringplus']].mean()
#
# print (daily_mean)
#
# daily_sum = data.groupby(data['time'].dt.date)[['wordcnt', 'itemcnt', 'Reputation_wordcnt', 'Reputation_itemcnt']].sum()
# print (daily_sum)
# # daily_metrics = data.groupby(['time']).agg({'sen':'mean', 'pos':'mean', 'neg':'mean', 'con':'mean', 'wordcnt':'sum', 'itemcnt':'sum', 'catastrophizing':'mean', 'dichotoreasoning':'mean', 'disqualpositive':'mean', 'emotionreasoning':'mean',
# #                                                 'fortunetelling':'mean', 'labeling':'mean', 'magnification':'mean', 'mentalfiltering':'mean', 'mindreading':'mean', 'overgeneralizing':'mean',
# #                                                 'personalizing':'mean', 'shouldment':'mean', 'exclusivereasoning':'mean', 'negativereasoning':'mean', 'mentalfilteringplus':'mean',
# #                                                 'Reputation_Score':'mean', 'Reputation_sen':'mean', 'Reputation_pos':'mean', 'Reputation_neg':'mean', 'Reputation_con':'mean', 'Reputation_wordcnt':'mean', 'Reputation_itemcnt':'mean', 'Reputation_catastrophizing':'mean',
# #                                                 'Reputation_dichotoreasoning':'mean', 'Reputation_disqualpositive':'mean', 'Reputation_emotionreasoning':'mean',
# #                                                 'Reputation_fortunetelling':'mean', 'Reputation_labeling':'mean', 'Reputation_magnification':'mean', 'Reputation_mentalfiltering':'mean',
# #                                                 'Reputation_mindreading':'mean', 'Reputation_overgeneralizing':'mean', 'Reputation_personalizing':'mean', 'Reputation_shouldment':'mean',
# #                                                 'Reputation_exclusivereasoning':'mean', 'Reputation_negativereasoning':'mean', 'Reputation_mentalfilteringplus':'mean'})
# daily_metrics  = pd.merge(daily_mean, daily_sum, on='time', how='outer')
# print (daily_metrics)
# Save the daily sum data as a new CSV
# daily_sum.to_csv('daily_sum_metrics_sum.csv')
daily_metrics.to_csv('daily_sum_metrics_mean.csv')

print("Daily metrics saved successfully.")
