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

daily_metrics.to_csv('daily_sum_metrics_mean.csv')

print("Daily metrics saved successfully.")
