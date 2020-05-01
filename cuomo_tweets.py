
## Scrape a single user's tweets; includes retweets

from twitterscraper.query import query_tweets_from_user
import pandas as pd

user = 'NYGovCuomo'

cuomo_tweets = query_tweets_from_user(user=user)
df_cuomo = pd.DataFrame(t.__dict__ for t in cuomo_tweets)
df_cuomo.to_csv('cuomo_twitter_scraped.csv')