# trump_tweeter

This script generates tweets with the help of markov chains based on trumps tweets.

Trump tweets that are used can be found here:
https://www.kaggle.com/kingburrito666/better-donald-trump-tweets

Run `generate_tweet.py` to generate tweets.
The generation of the markov chain, may take a while.

known bugs:
'&' are parsed incorrectly
links are sometimes parsed incorrectly
Special characters some times part of words. 
E.g.: 

Nice!" 

Making tweets look a bit wonky at times
