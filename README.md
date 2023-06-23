# Bitcoin-Reputation-Sentiment
Initial research repository for models correlating reputation system (on sentiment analysis) of bitcoin twitter dataset vs BTC pricing.
The project is the sub-set of the PhD dissertation topic as follows:

# Reputation System for Social Media Trend Analysis (applied to Finance) (might be interesting for SNET as well as other parties)

Project scope is on the verge options suggested as: [#281 and #282](https://github.com/singnet/reputation/issues/283)

Task breakdown:

Explore the communication graphs between team/group/channel/community members to identify trending topics vs. sentiment (and cognitive distortions?) about these topics, with topics primarily concerning particular market assets such as BTC, ETH, LTC, USDT, USDC, BUSD, ADA, TRX, etc.
be able to identify the temporally-stamped news streams in respect to specific assets
hourly (most better yet unlikely) ?
daily (better)?
weekly basis (as a last resort)?
render the "expression" ("popularity") plots on the timeline for each of the topics and combinations of them
render the sentiment and cognitive distortions metrics for each of the topics and combinations of them on the timeline
Explore reputations of the community members treating these topics
topic-specific reputation graphs (only in communications related to specific topic, mentioning it or pointing to ones mentioning it)
topic-unspecific reputation graphs (aggregating all of the above)
Assess the reliability of the topics vs. sentiment from perspective of reputations of the agents generating them (like it has been don in prior work)
generate adjusted sentiment/distortions metric trends over time with account to repuation
assess the resusts with some (TBD!!!???) criteria (one possibility is relate to actual pricing trends, so the sentiment may be "organic", or "manipulative", depending on the reputation score of the content source)
Come up with framework of community member reputation assessment along with communication topic trending and sentiment assessment
Run the experiments according to the above on
— simulation model
— Steemit (in the first place)
— Twitter/Reddit/Telegram/etc. (if time/resources permit)
Have the above implemented in either
— a) https://github.com/aigents/aigents-java/blob/master/src/main/java/net/webstructor/peer/Reputationer.java (can have full support from @akolonin , need to learn Java, no simulation present)
— b) https://github.com/singnet/reputation (all in Python, simulation prototype is in-place but might need to get changed)
— c) combine both (RS engine from a, simulation from b)
Explore the connections of the trends and sentiments/distortions to actual developments of financial markets and see if there are any causal connections and/or predictive power of having the socio-psychological trend/sentiment analytics applied to financial event predictions.
Resources:

https://aigents.medium.com - whatever is found on Reputation and Sentiment, especially on Steemit
https://steemit.com/@aigents - whatever is found on Reputation and Sentiment, especially on Steemit
https://github.com/Singularity-DAO/agi-fintech (talks 1 and 2) plus https://arxiv.org/abs/2204.12928
https://aigents.github.io/inlp/2022/ (talk 3 here) plus https://arxiv.org/abs/2204.10185 plus https://arxiv.org/abs/2204.12928
