import tweepy

consumer_key = 'RPBAX2N91ZW8ec1gu0wppLNZE'
consumer_secret = '1zB2pvEb3fBwyVVDkQG1MAFFVQBoodJwKtvLruidtdBugHLGgS'
access_token = '1462394680121995265-nxymbakV0u6Mcpe99NqlcPJuDqqCI5'
access_token_secret = 'wUiOXQOYi7BgU2wFqfJsTWdHzDnqmxUn3wkHOXfxHrLGQ'

# Authenticate to Twitter
def OAuth():
    try:
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        return auth
    except Exception as e :
        return None

auth = OAuth()   

# Create API object  
api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("Authentication OK")
    user = api.get_user(screen_name="ReseauxTelecom")
    print("User details:")
    x= str(user).split(",")
    for a in x:
        print(a+'\n')

except:
    print("Error during authentication")


