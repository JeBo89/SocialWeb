# First, let's query for all of the likes in your social
# network and store them in a slightly more convenient
# data structure as a dictionary keyed on each friend's name. Even testen
import facebook
from prettytable import PrettyTable
from collections import Counter

# Create a connection to the Graph API with your access token
token = 'EAACEdEose0cBAMsRp6SwJ9jwiAaysRXaZAeLk9JF1HEdbz1Rx3dreqbYBHgltRUxwbcgwdZBA6lyuE3qyriHh2IvYUZCGmVXbY2liTjgtLwBk44SjFoMu9u520Ps7ZB0rYoVPtTLRfJZBnVUNzT7jVFr8427X8DifswJEdtOJEler8fWDEijj5nsCdR7e7UwZD'
g = facebook.GraphAPI(access_token = token)

friends = g.get_connections(id = 'me', connection_name = 'friends')['data']

likes = { friend['name'] : g.get_connections(id = friend['id'], connection_name = 'likes')['data']
       for friend in friends }
#print likes

# Analyze all likes by frequency
friends_likes = Counter([like['name']
       for friend in likes
               for like in likes[friend]
                       if like.get('name')])

pt = PrettyTable(field_names=['Name', 'Freq'])
pt.align['Name'], pt.align['Freq'] = 'l', 'r'
[ pt.add_row(fl) for fl in friends_likes.most_common(10) ]

print '\n Top 10 likes amongst friends'
print pt

# Analyze all like categories by frequency (retrieving this information might take longer)
likes_categories = { like['name'] : g.get_object(id = like.get('id'), fields = 'category')
        for friend in likes
                for like in likes[friend]
                        if like.get('name') }

friends_likes_categories = Counter([like_category['category']
       for like_category in likes_categories.values()])

pt2 = PrettyTable(field_names=['Category', 'Freq'])
pt2.align['Category'], pt2.align['Freq'] = 'l', 'r'
[ pt2.add_row(flc) for flc in friends_likes_categories.most_common(10) ]

print "\n Top 10 like categories for friends"
print pt2
