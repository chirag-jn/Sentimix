from defaults import *

tweets = loadPickle('tweets')

for t in tweets:
    token_arr = t['tokens']
    