import string

tweet_a = "Everything is always too good to be true"

tweet_b = "I guess I have to try to go to bed early now"

#signature of a tweet

#remove whitespace e.g. letters_only = tweet.replace(" ","")

#filter


signature_tweet_a = ''.join(sorted(filter(str.isalpha, tweet_a).lower()))

signature_tweet_b = ''.join(sorted(filter(str.isalpha, tweet_b).lower()))

if (signature_tweet_a == signature_tweet_b):
    print ("The tweets are anagrams of each other")
else:
    print ("The tweets are not anagrams of each other")
