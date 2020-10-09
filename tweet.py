import tweepy #Importing tweepy's libary
import time #Allows us to control the access to the API's server

#Authentication Process
#The variables down below are what Twitter's API uses to verify the account
#(consumer_key, consumer_secret)
#(access_token, access_token_secret)
auth = tweepy.OAuthHandler('dBUR8EbNZrn2L8nbq60DzjW7S', 'jKmQrOelX0vF3FX1f6RLw0VNoaF0WICvDWm92aecM4EroxwStZ')
auth.set_access_token('2285259227-UdXlQGMn3SuO0Mqjg8GmVeKKnjvi7cKeqkihOV3', 'WsU8H7gWBj9S44YyRnOJ5EOGPj7sT4bRtexS9t2I9XgWw')

api = tweepy.API(auth) #This line of code allows for us to connect and use Twitter's API
user = api.me() #Gives us information regarding the user
#REMOVE the following hashtag to run certain commands with the API:
#print(user.name) #this action prints the name of the user
#print(user.screen_name) #this action prints the screenname of the user
#print(user.followers_count) #this action prints the number of followers

def limit_handle(cursor):          #This function allow us to make sure 
	try:                           #we are not going over Twitter's API
		while True:                #rate limit. It will pause instead of 
			yield cursor.next()    #getting errors. We don't want to abuse
	except tweepy.RateLimitError:  #the use of Twitter's servers.
		time.sleep(5000)    

#CheckFollowers
#for follower in tweepy.Cursor(api.followers).items() #Grab all the followers
	#print(follower.name) #We will be accessing the API multiple times

#FollowBack
#for follower in tweepy.Cursor(api.followers).items()
	#if follower.name == "userName" 
		#follower.follow() #this code block will follow a specified user(s)
	     
#SearchMachine
search_string = 'iOS 14' #Type in string form the topics we would like to favorite
for tweet in tweepy.Cursor(api.search, search_string).items(numbersOfTweets):
	try:
		tweet.favorite() #We can retweet or favorite
		print('Liked tweet')
	except tweepy.TweepError as e:
		print(e.reason)
	except StopIteration:
		break