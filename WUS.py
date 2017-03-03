"""WUS.py.

This script will take a tagged tweet to the set twitter account, and take the
location data given as an input. The location data will be used to retrieve
a Instagram photo from the given location and reply back to the user with
the retrieved image.
"""

import Tokens
import time
from twitter import Twitter, OAuth


# Set up twitter authentification
twitter = Twitter(
    retry=True,
    auth=OAuth(Tokens.token, Tokens.tokenSecret, Tokens.key, Tokens.keySecret))

#  Main Loop
tweetInOld = 0
while(1):
    time.sleep(60)
    tweetIn = twitter.statuses.home_timeline()
    if tweetInOld == 0:
        tweetInOld = tweetIn
        userName = tweetIn[0]['user']['name']
        tweetText = tweetIn[0]['text']
        print(userName, tweetText)
    elif (tweetIn[0]['user']['screen_name'] !=
          tweetInOld[0]['user']['screen_name']):
        # Checks to see if a new tweet it present
        tweetInOld = tweetIn
        userName = tweetIn[0]['user']['name']
        tweetText = tweetIn[0]['text']
        print(userName, tweetText)
