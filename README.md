# README

This app is an attempt to find out the Popularity and Sentiment Associated with
each presidential Candidate .  It generates two plots : The first one shows
which candidate is popular on Twitter to what extent The second plot shows a
score that shows the sentiment towards the canidate.  Positive score shows
positive sentiment Negative score shows negative sentiment. 0 is considered
neutral.

To run: Get twitter stream 
```sh
$ python twitterstream.py > trump_bernie_2016.txt python frequency.py AFINN-111.txt trump_bernie_2016.txt
```

### Key Results and takeaways
![Fig 1](https://github.com/myonlinecode1988/PresidentialSentiment/blob/master/presidential_mentions.png?raw=true)
**Fig 1: Most discussed candidate: Data represented as % of total mentions across all presidential candidates.**


![Fig 2](https://github.com/myonlinecode1988/PresidentialSentiment/blob/master/presidential_sentiments.png?raw=true)
**Fig 2: Most popular candidate: Data represented as sum of sentiment scores associated in words of tweet containing candidates' name**

- The first figure shows that on Feb 2016 (during time of data stream
collection), at least on Twittersphere, Bernie Sanders was most popular followed
by Donald Trump and Hillary Clinton. 

- The second figure shows the sentiment
associated with each of the presidential candidates. Bernie Sanders again took
the crown followed by Hillary Clinton and Donald Trump.


This data is telling because it did show a good amount of  popularity of Donald
Trump in social media (before Iowa caususes) when most news outlets (both
conservative-leaning and liberal-leaning) sources did not take Trump as a
serious contender and the general perception was that Jeb Bush is going to win
the primaries.

As a self critique, there is no baseline score of sentiment and the data may have
been colored due to primary debates being aired at the time. Also larger sample size
would have been nice.
