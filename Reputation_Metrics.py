import pandas as pd

# Step 1: Load the original dataset and keep only the required columns
data = pd.read_csv('Crypto_twitter_full.csv', usecols=['type', 'link', 'time', 'text', 'sen', 'pos', 'neg', 'con', 'wordcnt', 'itemcnt', 'catastrophizing',	'dichotoreasoning',
                                                       'disqualpositive', 'emotionreasoning','fortunetelling', 'labeling', 'magnification', 'mentalfiltering', 'mindreading',
                                                       'overgeneralizing', 'personalizing',	'shouldment', 'exclusivereasoning', 'negativereasoning', 'mentalfilteringplus'], encoding='latin1', low_memory=False, dtype={'pos': str})

# Step 2: Keep only twitter from the 'type' column
data = data[data['type'] == 'twitter']

# Step 3: Rename the 'link' column to 'Channels' and clean the values
data['Channels'] = data['link'].str.replace('https://twitter.com/', '@', regex=True)
data = data.drop(columns=['link'])

# Step 4: Set 'time' column as the index
data['time'] = pd.to_datetime(data['time'])
data.set_index('time', inplace=True)

# Step 5: Load the 'Reputation' dataset and perform a lookup to get the Reputation_Score
reputation_data = pd.read_csv('Reputation.csv')

# Convert both 'Channels' columns to lowercase for case-insensitive matching
data['Channels'] = data['Channels'].str.lower()
reputation_data['Channels'] = reputation_data['Channels'].str.lower()

channels_reputation = dict(zip(reputation_data['Channels'], reputation_data['Reputation']))
data['Reputation_Score'] = data['Channels'].map(channels_reputation)

# Step 6: Convert metric columns to numeric (float)
data['sen'] = pd.to_numeric(data['sen'], errors='coerce')  # Convert non-numeric values to NaN
data['pos'] = pd.to_numeric(data['pos'], errors='coerce')
data['neg'] = pd.to_numeric(data['neg'], errors='coerce')
data['con'] = pd.to_numeric(data['con'], errors='coerce')
data['wordcnt'] = pd.to_numeric(data['wordcnt'], errors='coerce')
data['itemcnt'] = pd.to_numeric(data['itemcnt'], errors='coerce')
data['catastrophizing'] = pd.to_numeric(data['catastrophizing'], errors='coerce')
data['dichotoreasoning'] = pd.to_numeric(data['dichotoreasoning'], errors='coerce')
data['disqualpositive'] = pd.to_numeric(data['disqualpositive'], errors='coerce')
data['emotionreasoning'] = pd.to_numeric(data['emotionreasoning'], errors='coerce')
data['fortunetelling'] = pd.to_numeric(data['fortunetelling'], errors='coerce')
data['labeling'] = pd.to_numeric(data['labeling'], errors='coerce')
data['magnification'] = pd.to_numeric(data['magnification'], errors='coerce')
data['mentalfiltering'] = pd.to_numeric(data['mentalfiltering'], errors='coerce')
data['mindreading'] = pd.to_numeric(data['mindreading'], errors='coerce')
data['overgeneralizing'] = pd.to_numeric(data['overgeneralizing'], errors='coerce')
data['personalizing'] = pd.to_numeric(data['personalizing'], errors='coerce')
data['shouldment'] = pd.to_numeric(data['shouldment'], errors='coerce')
data['exclusivereasoning'] = pd.to_numeric(data['exclusivereasoning'], errors='coerce')
data['negativereasoning'] = pd.to_numeric(data['negativereasoning'], errors='coerce')
data['mentalfilteringplus'] = pd.to_numeric(data['mentalfilteringplus'], errors='coerce')

# Step 7: Calculate 'Reputation_All' as Reputation_Score * All[object]
data['Reputation_sen'] = (data['Reputation_Score'] + 1) * data['sen']
data['Reputation_pos'] = (data['Reputation_Score'] + 1) * data['pos']
data['Reputation_neg'] = (data['Reputation_Score'] + 1) * data['neg']
data['Reputation_con'] = (data['Reputation_Score'] + 1) * data['con']
data['Reputation_wordcnt'] = (data['Reputation_Score'] + 1) * data['wordcnt']
data['Reputation_itemcnt'] = (data['Reputation_Score'] + 1) * data['itemcnt']
data['Reputation_catastrophizing'] = (data['Reputation_Score'] + 1) * data['catastrophizing']
data['Reputation_dichotoreasoning'] = (data['Reputation_Score'] + 1) * data['dichotoreasoning']
data['Reputation_disqualpositive'] = (data['Reputation_Score'] + 1) * data['disqualpositive']
data['Reputation_emotionreasoning'] = (data['Reputation_Score'] + 1) * data['emotionreasoning']
data['Reputation_fortunetelling'] = (data['Reputation_Score'] + 1) * data['fortunetelling']
data['Reputation_labeling'] = (data['Reputation_Score'] + 1) * data['labeling']
data['Reputation_magnification'] = (data['Reputation_Score'] + 1) * data['magnification']
data['Reputation_mentalfiltering'] = (data['Reputation_Score'] + 1) * data['mentalfiltering']
data['Reputation_mindreading'] = (data['Reputation_Score'] + 1) * data['mindreading']
data['Reputation_overgeneralizing'] = (data['Reputation_Score'] + 1) * data['overgeneralizing']
data['Reputation_personalizing'] = (data['Reputation_Score'] + 1) * data['personalizing']
data['Reputation_shouldment'] = (data['Reputation_Score'] + 1) * data['shouldment']
data['Reputation_exclusivereasoning'] = (data['Reputation_Score'] + 1) * data['exclusivereasoning']
data['Reputation_negativereasoning'] = (data['Reputation_Score'] + 1) * data['negativereasoning']
data['Reputation_mentalfilteringplus'] = (data['Reputation_Score'] + 1) * data['mentalfilteringplus']

# Step 8: Save the dataset as 'reputation_sentiment.csv'
data.to_csv('reputation_all_updated.csv')
