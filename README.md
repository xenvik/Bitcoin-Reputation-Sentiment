# Bitcoin-Reputation-Sentiment 
Initial research repository for models correlating reputation system (on sentiment analysis) of bitcoin twitter dataset vs BTC pricing.
The project is the sub-set of the PhD dissertation topic as follows:

# Reputation System for Social Media Trend Analysis (applied to Finance) (might be interesting for SNET as well as other parties)

Project scope is on the verge options suggested as: (https://github.com/singnet/reputation/issues/283)


# Dataset

Two kinds of metrics were derived from the online social media data:
public posts from about 80 channels on [Twitter] relevant to crypto market for 1 year and six months starting June 2021.
First, it was the conventional sentiment scores, computed as described below. Second, it was the “[cognitive behavioral schemata]” (CBS) patterns. The overall volume of the media content was exceeding 397,117 posts across 48824 channels. Dataset contains all 21 metrics including CBS, sentiment scores and tweet description alongwith timestamp, word count and item count.

Apart from that BTC price and volume data was collected for price and volume trens during June 2021 to December 2022. This dataset contains BTC price open, close, volume, high/Low of BTC/USD price and timestamp.

# Methodology 

The project flow can be described into following steps:
* Reputation Scoring of the Twitter Data
* Implementing Reputation scores with Sentiment and CBS metrics.
* Performing Correlation Analysis and comparing results

## Reputation Scoring of the Twitter Data

A liquid rank reputation model has been developed. The model makes the use case simple, also considering the restraints of the dataset a simple computational model of reputation is calculated as 

                          [  Rj = ∑(Ri∗Vijt) ]
where Vijt here is an implicit rating (positive) as the number of mentions by each channel for node j (Twitter channel) being rated, node i supplying the rating and time t. Reputation is calculated for channels, but it is assumed that each channel plays a multi-agent social network role for each user account. Nodes during their operation, so that their artifacts can be indirectly rated mentioned on Twitter network cryptocurrency feed by the channels which were selected as initial inputs (higher-order friends) to fetch the dataset in the given time frame. The final results are normalised to [0,1] range.

## Implementing Reputation scores with Sentiment and CBS metrics

For Reputation metrics scoring all the 21 metrics including CBS, sentiment metrics [sen, pos, neg, con] with word count and item count for each user tweet are calculated using 
                       [ Reputation_'metric' = 'metric' * (1 + Aggregated Reputation Score)]

The dataset has been been aggregated day wise, after all the channels has been mapped with their respective reputation score. Alonwith that we have also agregated BTC-USD data day wise to correlate the price and volume trend with Reputation Metrics between June 2022 to December 2022.

## Performing Correlation Analysis and comparing results

The final results are processed using Pearson Correlation analysis for:
* Metrics vs Price Change and Volume
* Reputation Metrics vs Price Change and Volume

All the metrics has been aggregated day wise to have daily results and predictions. Hence for impact of above metrics we have further calculated Pearson Correlation:
* With -1 Day Lagged BTC-USD Data
* Without Lag BTC-USD Data

# Results
* Reputation Scoring have fine tuned the Correlation results than the normal metrics. We have seen positive results of application of Reputation System on the Metrics for Price Predictions.
* Results show that the correlation between without lag data is higher than the lagged BTC Price change and Volume.

