README

This app is an attempt to find out the Popularity and Sentiment Associated with each presidential Candidate . 

It generates two plots : 
The first one shows which candidate is popular on Twitter to what extent
The second plot shows a score that shows the sentiment towards the canidate.

Positive score shows positive sentiment
Negative score shows negative sentimen
0 is considered neutral


To run:
Get twitter stream
python twitterstream.py > trump_bernie_2016.txt
python frequency.py AFINN-111.txt trump_bernie_2016.txt
