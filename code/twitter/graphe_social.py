from networkx.classes.function import edges
import tweepy
import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt


consumer_key = 'RPBAX2N91ZW8ec1gu0wppLNZE'
consumer_secret = '1zB2pvEb3fBwyVVDkQG1MAFFVQBoodJwKtvLruidtdBugHLGgS'
access_token = '1462394680121995265-nxymbakV0u6Mcpe99NqlcPJuDqqCI5'
access_token_secret = 'wUiOXQOYi7BgU2wFqfJsTWdHzDnqmxUn3wkHOXfxHrLGQ'


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)


me = api.get_user(screen_name = 'arij42628172')
print(me)
me.id

user_list = [1462394680121995265]
follower_list = []
for user in user_list:
    followers = []
    try:
        for page in tweepy.Cursor(api.get_follower_ids, screen_name = 'arij42628172').pages():
            followers.extend(page)
            print(len(followers))
    except tweepy.TwitterServerError:
        print("error")
        continue
    follower_list.append(followers)

    fichier = open("followrs.txt", "w")
    for f in followers:
        print(f)
        fichier.write(str(me.id)+"  "+ str(f)+"\n")
    fichier.close()

df = pd.DataFrame(columns=['source','target']) 
df['target'] = follower_list[0] 
df['source'] = 1462394680121995265


G = nx.from_pandas_edgelist(df, 'source', 'target') 
pos = nx.spring_layout(G)


f, ax = plt.subplots(figsize=(10, 10))
plt.style.use('ggplot')
nodes = nx.draw_networkx_nodes(G, pos, alpha=0.8)


nx.draw_networkx_labels(G, pos, font_size=8)
nx.draw_networkx_edges(G, pos, width=1.0, alpha=0.2)

plt.show()
print(G)






