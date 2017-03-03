"""WUS.py.

This script will take a tagged tweet to the set twitter account, and take the
location data given as an input. The location data will be used to retrieve
a Instagram photo from the given location and reply back to the user with
the retrieved image.
"""

from Tokens import token, tokenSecret, key, keySecret
import time
from twitter import Twitter, OAuth
import re

# Set up twitter authentification
twitter = Twitter(
    retry=True,
    auth=OAuth(token, tokenSecret, key, keySecret))

#  Main Loop
tweetInOld = 0
calloutCheck = 0

while(1):
    time.sleep(3)  # API Timer delay
    tweetIn = twitter.search.tweets(q='@ksu_bell')
    # print(tweetIn)  # Uncomment to check current read tweet JSON data
    # tweetIn = twitter.statuses.home_timeline()  # Pulls current timeline
    """Not quite sure how to make these two if statements into one, need the
    first on right now to take care of the first iteration when the
    tweetInOld is not valid for JSON extraction"""
    if tweetInOld == 0:  # First iteration
        tweetInOld = tweetIn
        userName = tweetIn['statuses'][0]['user']['name']  # Most recent tweet
        tweetText = tweetIn['statuses'][0]['text']
        normalText = str(tweetText)  # Makes JSON a string
        # print(normalText.lower())  # Uncomment for testing
        # print(userName, tweetText)  # Uncomment for testing
        calloutCheck = re.search(r'@ksu_bell', normalText.lower())
    # Checks to see if a new tweet it present
    elif (tweetIn['statuses'][0]['user']['name'] !=
          tweetInOld['statuses'][0]['user']['name']):
        tweetInOld = tweetIn
        userName = tweetIn['statuses'][0]['user']['name']  # Most recent tweet
        tweetText = tweetIn['statuses'][0]['text']
        normalText = str(tweetText)
        calloutCheck = re.search(r'@ksu_bell', normalText.lower())
    if calloutCheck != 0:
        """This section of the code will search the tweet for any format
        of a location input which will be used to get lat and long from
        the Google API"""
        handle = calloutCheck.group()  # If executed, handle is present (test)
        print(handle)  # Test
        calloutCheck = 0  # Reset the calloutCheck variable to prevent loops
