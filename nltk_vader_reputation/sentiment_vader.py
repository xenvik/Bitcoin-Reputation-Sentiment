# import pandas as pd
#
# df = pd.read_csv('bitcoin_twitter.csv', sep=',', low_memory=False)
#
# # datatop = df.head()
# #
# # print (datatop)
#
# for col in df.columns:
#     print (col)
#

import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
import pandas as pd

# Download the VADER lexicon if not already downloaded
nltk.download('vader_lexicon')

# Initialize the VADER sentiment analyzer
sia = SentimentIntensityAnalyzer()

# Load the dataset into a pandas DataFrame
df = pd.read_csv('bitcoin_twitter.csv', sep=',', low_memory=False)

# Create an empty column to store the sentiment scores
df['sentiment_score'] = 0.0

# Iterate over each row in the DataFrame
for index, row in df.iterrows():
    # Get the tweet text from the 'text' column
    tweet_text = row['text']

    # Calculate the sentiment score using VADER
    sentiment_scores = sia.polarity_scores(tweet_text)

    # Store the compound sentiment score in the 'sentiment_score' column
    df.at[index, 'sentiment_score'] = sentiment_scores['compound']

# Print the updated DataFrame
print(df)
df.to_csv('sentiment_scores.csv', index=False)