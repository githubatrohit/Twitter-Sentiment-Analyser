from textblob import TextBlob
import sys, tweepy
import matplotlib.pyplot as plt

#Hidden for security puproses
consumerKey       = "XXX"
consumerSecret    = "XXX"
accessToken       = "XXX"
accessTokenSecret = "XXX"


auth = tweepy.OAuthHandler(consumerKey,consumerSecret)
auth.set_access_token(accessToken, accessTokenSecret)
api = tweepy.API(auth)

#Checking the connection with twitter 
#try:
#    api.verify_credentials()
#    print("Authentication successful")
#except:
#    print("Error during authentication")

    

def percentage(fraction , total):
    return 100 * float(fraction)/float(total)


toSearch  = input("Enter the keyword/topic to analyze: ")
noOfTerms = int(input("How many tweets to analyze?: "))

#getting the tweets 
tweets = tweepy.Cursor(api.search_tweets, q=toSearch).items(noOfTerms)


#variables to store the polarity of the analyzed tweets
positive = 0
negative = 0
neutral  = 0 
polarity = 0


for tweet in tweets:
    analysis = TextBlob(tweet.text)
    polarity += analysis.sentiment.polarityn #overall polarity of the tweets

    #adding positive, negative, neutral polarity seperately
    if(analysis.sentiment.polarity == 0):
        neutral += 1

    elif(analysis.sentiment.polarity < 0.00):
        negative += 1

    elif(analysis.sentiment.polarity > 0.00):
        positive += 1


positive = percentage(positive, noOfTerms)
neutral  = percentage(neutral,  noOfTerms)
negative = percentage(negative, noOfTerms)
polarity = percentage(polarity, noOfTerms)


positive = format(positive, '.2f')
neutral  = format(neutral,  '.2f')
negative = format(negative, '.2f')

print("-----Overall sentiment Of people on " + toSearch + " after analyzing " + str(noOfTerms) + " tweets.-----")

if(polarity == 0):
    print("=>Neutral")
elif(polarity < 0):
    print("=>Negative")
elif(polarity > 0):
    print("=>Positive")

#plotting the sentiments as piechart through the matplotlib library
labels = ['Positive [' +str(positive)+'%]', 'Neutral [' +str(neutral) + '%]', 'Negative[' +str(negative) + '%]']
sentiment = [positive, neutral, negative]
colours = ['yellowgreen', 'blue', 'red']
patches, texts = plt.pie(sentiment, colors = colours, startangle=90)
plt.legend(patches, labels, loc='best')
plt.title('Sentiment Of people on ' + toSearch + ' by analyzing ' + str(noOfTerms) + ' tweets.')
plt.axis('equal')
plt.tight_layout()
plt.show()
    
