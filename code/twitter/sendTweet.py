import tweepy

consumer_key = 'RPBAX2N91ZW8ec1gu0wppLNZE'
consumer_secret = '1zB2pvEb3fBwyVVDkQG1MAFFVQBoodJwKtvLruidtdBugHLGgS'
access_token = '1462394680121995265-nxymbakV0u6Mcpe99NqlcPJuDqqCI5'
access_token_secret = 'wUiOXQOYi7BgU2wFqfJsTWdHzDnqmxUn3wkHOXfxHrLGQ'
def OAuth():
    try:

        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        return auth
    except Exception as e :
        return None

auth = OAuth()     
 
api = tweepy.API(auth)
api.update_status("Le Tweet est envoyé en utilisant notre code Python!!!")
print("Le Tweet est envoyé en utilisant notre code Python!!!")