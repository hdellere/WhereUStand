"""WUS.py.

This script will take a tagged tweet to the set twitter account, and take the
location data given as an input. The location data will be used to retrieve
a Instagram photo from the given location and reply back to the user with
the retrieved image.
"""

import Tokens
import time
from twitter import Twitter, OAuth
tweetInOld = 0
# Set up twitter authentification
twitter = Twitter(
    retry=True,
    auth=OAuth(Tokens.token, Tokens.tokenSecret, Tokens.key, Tokens.keySecret))

#  Main Loop
while(1):
    time.sleep(120)
    tweetIn = twitter.statuses.home_timeline(count=1)
    if (tweetIn[0]['user']['screen_name'] !=
       tweetInOld[0]['user']['screen_name']):
            # Checks to see if a new tweet it present
        tweetInOld = tweetIn
        userName = tweetIn[0]['user']['name']
        tweetText = tweetIn[0]['text']
        print(userName, tweetText)
