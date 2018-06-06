from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
import sentiment_mod as s
#consumer key, consumer secret, access token, access secret.

ckey="4WiHe6rR2EfCkEUDqm6EFpQ9d"
csecret="HlCkqEIS5F2QqXlI6cD2Ila2J3djhMvXQFllUkyNrsqBRHhBpW"
atoken="988671013540986880-50Tp7EuCeis4gw3LmpJgy3YQlyCGmHo"
asecret="kxz45Tz3ig7iiD0r3CzsO4nz0pNkquYxqdlqZ2Fdl0kqq"

class listener(StreamListener):

    def on_data(self, data):
        try:
            all_data = json.loads(data)
            tweet = all_data["text"]
            sentiment_value,confidence=s.sentiment(tweet)
            print(tweet,sentiment_value,confidence)
            
            if confidence*100>=80:
                output=open("twitter-out.txt","a")
                output.write(sentiment_value)
                output.write("/n")
                output.close()
            return True
        except:
               return True
    def on_error(self, status):
        print (status)

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

twitterStream = Stream(auth, listener())
twitterStream.filter(track=["obama"])
