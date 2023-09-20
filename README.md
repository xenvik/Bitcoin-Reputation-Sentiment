# Bitcoin-Reputation-Sentiment 
Initial research repository for models correlating reputation system (on sentiment analysis) of bitcoin twitter dataset vs BTC pricing.
The project is the sub-set of the PhD dissertation topic as follows:

## Reputation System for Social Media Trend Analysis (applied to Finance) (might be interesting for SNET as well as other parties)

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
* Performing Correlation Analysis and Results

## Reputation Scoring of the Twitter Data

A liquid rank reputation model has been developed. The model makes the use case simple, also considering the restraints of the dataset a simple computational model of reputation is calculated as 

####                          [  Rjt = ∑(Rit ∗ Vijt) ]
where Vijt here is an implicit rating (positive) as the number of mentions by each channel for node j (Twitter channel) being rated, node i supplying the rating and time t. Reputation is calculated for channels, but it is assumed that each channel plays a multi-agent social network role for each user account. Nodes during their operation, so that their artifacts can be indirectly rated mentioned on Twitter network cryptocurrency feed by the channels which were selected as initial inputs (higher-order friends) to fetch the dataset in the given time frame. The final results are normalised to [0,1] range.

## Implementing Reputation scores with Sentiment and CBS metrics

For Reputation metrics scoring all the 21 metrics including CBS, sentiment metrics [sen, pos, neg, con] with word count and item count for each user tweet are calculated using
####        [ Reputation_'metric' = 'metric' * (1 + Aggregated Reputation Score)]

The dataset has been been aggregated day wise, after all the channels has been mapped with their respective reputation score. Alonwith that we have also agregated BTC-USD data day wise to correlate the price and volume trend with Reputation Metrics between June 2022 to December 2022.

## Performing Correlation Analysis and Results

The final results are processed using Pearson Correlation analysis for:
* Metrics vs Price Change and Volume
* Reputation Metrics vs Price Change and Volume

All the metrics has been aggregated day wise to have daily results and predictions. Hence for impact of above metrics we have further calculated Pearson Correlation:
* With -1 Day Lagged BTC-USD Data
* Without Lag BTC-USD Data

### Following are the Results from Pearson Correlation Analysis 
* Pearson Correlations for Metrics and Reputation Metrics without lag
![Latest_wo_lag](https://github.com/xenvik/Bitcoin-Reputation-Sentiment/assets/55597813/c12006bf-447e-4aa2-99c4-092406233af1)

* Pearson Correlations for Metrics and Reputation Metrics with lag
![Latest_lagged](https://github.com/xenvik/Bitcoin-Reputation-Sentiment/assets/55597813/6b883e52-fae7-4c98-a77a-9adb78fee6f7)

#### As we see the results have fine PC scores but not any major impact can be withdrawn from it. So, we further study to the process of finding what we called synthetic additive cause indicator (SACI) relying on the whole scope of source metrics being treated as a hypothetical causes. The probabilistic logic treats addition as logical disjunction and multiplication as logical conjunction. In this work we were exploring only the disjunctive version of it, so the assembly of the integrative SACI was involving addition of the perspective causes in order to maximize the correlation with the effect at a particular target shift/lag. See the discussion on the SACI performance presented in the following section.

### Synthetic Additive Cause Indicator: SACI
The temporal causation study was run evaluating with -1 Day lags and without lag for all Metrics and Reputation Metrics computing mutual Pearson correlation (PC) between each of the potential causes and the price difference and retaining the “correlation weights” of the computed value P(l,m) for lag l and metric m. Also, as the channels c were optionally weighted with the “Reputation weight” as R(c) according to the mentions in twitter feed present on such time intervals, as shown on Figure 1, below. Then, for lag l, the compound SACI metric time series: 
#### Y(l,d) = ΣX(c,m,d) *P(l,c,m) *R(c) 
for day d have been built from the original raw metrics or reputation metrics X(c,m,d) in case of reputation scored metrics. The compound SACI metric building process was implemented
starting from channels with the highest R(c) and P(l,c,m) adding ingredients up to
Y(l,d) as the correlation between the target price difference, volume function and related metrics. Figure 2 and 3 gives the final SACI (additive) for Price Change PC and Volume PC of all the metrics and reputation metrics with/out lag of -1 Day.

* Figure 1: Reputation Weights R(c) (scores) of Top 50 channels for illustration
![reputation](https://github.com/xenvik/Bitcoin-Reputation-Sentiment/assets/55597813/b4a75f51-9ea5-44d7-9661-863f10417e4f)

* Figure 2: SACI for Price Change PC including sen, sen lagged, pos, pos lagged, neg, neg lagged, con, con lagged, Counts_Daily (wordcnt+itemcnt), Counts_lagged, CBS (cognitive behavioral schemata), CBS lagged, CBS+sen, CBS+sen lagged, CBS+sen+Counts_Daily, CBS+sen+Counts_Daily lagged
![SACI_Price_Change](https://github.com/xenvik/Bitcoin-Reputation-Sentiment/assets/55597813/756a256a-4b0d-4f7c-91d6-bda39f257c6d)

* Figure 3: SACI for Volume PC including sen, sen lagged, pos, pos lagged, neg, neg lagged, con, con lagged, Counts_Daily (wordcnt+itemcnt), Counts_lagged, CBS (cognitive behavioral schemata), CBS lagged, CBS+sen, CBS+sen lagged, CBS+sen+Counts_Daily, CBS+sen+Counts_Daily lagged
![SACI_Volume](https://github.com/xenvik/Bitcoin-Reputation-Sentiment/assets/55597813/256c6825-a939-41ba-b077-493522b533c1)

### Results
* Reputation Scoring have fine tuned the Correlation results than the normal metrics. We have seen positive results of application of Reputation System on the Metrics for Price Predictions.
* Results show that the correlation between without lag data is higher than the lagged BTC Price change and Volume.
* Best correlation are shown in metrics namely sen, pos, neg (inverse relation of sentiments), con, wordcnt, itemcnt (all > 0.1 PC) on Volume of BTC
* The above metrics have seen improved correlations with reputation metrics on Volume BTC repsectively as Reputation_sen, Reputation_pos, Reputation_neg, Reputation_con, Reputation_wordcnt and Reputation_itemcnt. 
* Study SACI we have found the final additive PC for Volume vs metrics and reputation metrics have shown some impactful scores (highest been > 0.85)
* SACI shows the cummulative effect of CBS+sen+Counts_Daily are the best indicator of impact of social media on prediction of BTC Trade Volume

# Conclusion
* We see that the major impact of social media metrics (cumulative) are more correlated to BTC Trade Volume through SACI model reaching as high as 0.86 for reputation metrics
* Though the impact of Reputation model is negligible in normal Pearson Correlations and in SACI (to order of 1-2%) the final results are been fine tuned and bettered by Reputation Model which is a positive sign for the research and further development.
* We have seen the most important metrics are Sentiment metrics (sen, pos, neg and con) followed by Counts daily (frequency and words) and cumulative CBS metrics

# Future Scope
* Reputation Model should further be tested on different dataset and more metrics of social media user profile to fine tune Reputation Scoring Model.
* Another dimension is to test on more cryptocurrencies (stable) to see the active impact of social media on Price and Volume of same.
