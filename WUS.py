"""WUS.py.

This script will take a tagged tweet to the set twitter account, and take the
location data given as an input. The location data will be used to retrieve
a Instagram photo from the given location and reply back to the user with
the retrieved image.
"""

import Tokens
import time
from twitter import Twitter, OAuth
import re

# Set up twitter authentification
twitter = Twitter(
    retry=True,
    auth=OAuth(Tokens.token, Tokens.tokenSecret, Tokens.key, Tokens.keySecret))

#  Main Loop
tweetInOld = 0
while(1):
    time.sleep(75)  # API Timer delay
    tweetIn = twitter.statuses.home_timeline()  # Pulls current timeline
    """Not quite sure how to make these two if statements into one, need the
    first on right now to take care of the first iteration when the
    tweetInOld is not valid for JSON extraction"""
    if tweetInOld == 0:  # First iteration
        tweetInOld = tweetIn
        userName = tweetIn[0]['user']['name']  # Most recent tweet on timeline
        tweetText = tweetIn[0]['text']
        normalText = str(tweetText)  # Makes JSON a string
        print(normalText.lower())  # Test
        print(userName, tweetText)  # Test
        calloutCheck = re.search(r'@ksu_bell', normalText.lower())
    # Checks to see if a new tweet it present
    elif (tweetIn[0]['user']['screen_name'] !=
          tweetInOld[0]['user']['screen_name']):
        tweetInOld = tweetIn
        userName = tweetIn[0]['user']['name']
        tweetText = tweetIn[0]['text']
        normalText = str(tweetText)
        calloutCheck = re.search(r'@ksu_bell', normalText.lower())
    if calloutCheck:
        handle = calloutCheck.group()  # If executed, handle is present
        print(handle)
