import re
import pandas as pd
import numpy as np
from tqdm import tqdm
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt
import networkx as nx

# Read the Bitcoin Twitter dataset into a pandas DataFrame
tweets_raw_file = 'Bitcoin_tweets.csv'
tweets_clean_file = 'Bitcoin_tweets_clean.csv'
bit_price_file2 = 'BTC-USD_1h.csv'

df_raw = pd.read_csv(tweets_raw_file, low_memory=False)
print(df_raw.shape)
df_raw.head(5)

# Clean df
df_raw = df_raw.sort_values(by='date')
dd = df_raw.sample(frac=0.01, replace=False, random_state=1)
dd.reset_index(inplace=True)
for i, s in enumerate(tqdm(dd['text'], position=0, leave=True)):
    text = str(dd.loc[i, 'text'])
    text = text.replace("#", "")
    text = re.sub('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', '', text, flags=re.MULTILINE)
    text = re.sub('@\\w+ *', '', text, flags=re.MULTILINE)
    dd.loc[i, 'text'] = text

dd.to_csv(tweets_clean_file, header=True, encoding='utf-8', index=False)

df_clean = pd.read_csv(tweets_clean_file)

# Initialize the sentiment analyzer
analyzer = SentimentIntensityAnalyzer()

# Calculate compound sentiment scores for each tweet
compound = []
for i, s in enumerate(tqdm(df_clean['text'], position=0, leave=True)):
    vs = analyzer.polarity_scores(str(s))
    compound.append(vs["compound"])
df_clean["compound"] = compound
df_clean.head(2)

# Calculate reputation scores using the reputation_calculation function
def reputation_calculation(G, damping_factor=0.85, max_iterations=100):
    for _ in range(max_iterations):
        convergence = True
        for node in G.nodes:
            reputation_score = 0.0
            for neighbor in G.predecessors(node):
                edge_weight = G.edges[neighbor, node]['weight']
                neighbor_reputation = G.nodes[neighbor]['reputation']
                reputation_score += neighbor_reputation * edge_weight
            if 'verified' in G.nodes[node] and G.nodes[node]['verified']:
                reputation_score += neighbor_reputation * 1.1  # Add Fij = 1.1 if user_verified is True
            reputation_score = damping_factor * reputation_score
            if abs(G.nodes[node]['reputation'] - reputation_score) > 0.0001:  # Convergence check
                convergence = False
            G.nodes[node]['reputation'] = reputation_score

        # Normalize the reputation scores using Min-Max scaling
        min_score = min(G.nodes[node]['reputation'] for node in G.nodes)
        max_score = max(G.nodes[node]['reputation'] for node in G.nodes)

        for node in G.nodes:
            reputation_score = G.nodes[node]['reputation']
            normalized_score = (reputation_score - min_score) / (max_score - min_score)
            G.nodes[node]['reputation'] = normalized_score + 1  # Add base value of 1 to reputation score

        if convergence:
            break

    return G

# Create an empty directed graph
G = nx.DiGraph()

# Add edges to the graph based on the user relationships in the dataset
for index, row in df_clean.iterrows():
    user_name = row['user_name']
    user_followers = row['user_followers']
    user_verified = row['user_verified']
    G.add_edge(user_name, user_name, weight=user_followers)  # Self-edge with weight as user_followers
    if user_verified:
        G.nodes[user_name]['verified'] = True

# Set initial reputation score for all nodes as 1.0
for node in G.nodes:
    G.nodes[node]['reputation'] = 1.0

# Call the reputation_calculation function to calculate reputation scores
reputation_graph = reputation_calculation(G)

# Extract the reputation scores from the graph
reputation_dict = {node: reputation_graph.nodes[node]['reputation'] for node in reputation_graph.nodes}

# Add the reputation scores to the DataFrame
df_clean['reputation'] = df_clean['user_name'].map(reputation_dict)

scores = []
for i, s in tqdm(df_clean.iterrows(), total=df_clean.shape[0], position=0, leave=True):
    try:
        scores.append(
            s["compound"] * ((int(s["user_followers"]))) * ((int(s["user_favourites"]) + 1) / int(
                s['user_followers'] + 1)) * ((int(s["is_retweet"]) + 1)))
    except:
        scores.append(np.nan)
df_clean["score"] = scores
df_clean.head(2)

df_price = pd.read_csv(bit_price_file2)
df_price['Date'] = pd.to_datetime(df_price['Date'])
df_price.head(2)

df_clean = df_clean.drop_duplicates()
tweets = df_clean.copy()
tweets['date'] = pd.to_datetime(tweets['date'])
tweets.index = tweets['date']

tweets_grouped = tweets.resample('1h').sum()

crypto_usd = df_price.copy()
crypto_usd['Date'] = pd.to_datetime(crypto_usd['Date'], unit='s')
crypto_usd.index = crypto_usd['Date']
crypto_usd_grouped = crypto_usd.resample('H')['Close'].mean()

def crosscorr(datax, datay, lag=0, method="pearson"):
    return datax.corrwith(datay.shift(lag), method=method)['score']

beginning = max(tweets_grouped.index.min(), crypto_usd_grouped.index.min())
end = min(tweets_grouped.index.max(), crypto_usd_grouped.index.max())
tweets_grouped = tweets_grouped[beginning:end]
crypto_usd_grouped = crypto_usd_grouped[beginning:end]

# Plot normalized sentiment score vs BTC price
fig, ax1 = plt.subplots(figsize=(20, 10))
ax1.set_title("Normalized Sentiment Score vs BTC Price", fontsize=18)
ax1.tick_params(labelsize=14)
ax2 = ax1.twinx()
ax2.tick_params(labelsize=14)

# Normalize the sentiment score
min_score = min(tweets_grouped['score'])
max_score = max(tweets_grouped['score'])
normalized_score = (tweets_grouped['score'] - min_score) / (max_score - min_score)

ax1.plot(crypto_usd_grouped.index, crypto_usd_grouped, 'r-', linewidth=0.5)
ax1.set_ylabel("Price ($)", fontsize=16, color='r')
ax2.plot(tweets_grouped.index, normalized_score, 'b-')
ax2.set_ylabel("Normalized Sentiment Score", fontsize=16, color='b')

plt.savefig('normalized_sentiment_price.png')

# Plot normalized reputation sentiment score vs BTC price
fig, ax3 = plt.subplots(figsize=(20, 10))
ax3.set_title("Normalized Reputation Sentiment Score vs BTC Price", fontsize=18)
ax3.tick_params(labelsize=14)
ax4 = ax3.twinx()
ax4.tick_params(labelsize=14)

# Normalize the reputation sentiment score
min_reputation_score = min(tweets_grouped['reputation'])
max_reputation_score = max(tweets_grouped['reputation'])
normalized_reputation_score = (tweets_grouped['reputation'] - min_reputation_score) / (max_reputation_score - min_reputation_score)

ax3.plot(crypto_usd_grouped.index, crypto_usd_grouped, 'r-', linewidth=0.5)
ax3.set_ylabel("Price ($)", fontsize=16, color='r')
ax4.plot(tweets_grouped.index, normalized_reputation_score, 'g-')
ax4.set_ylabel("Normalized Reputation Sentiment Score", fontsize=16, color='g')

plt.savefig('normalized_reputation_sentiment_price.png')
