import networkx as nx 
from networkx.readwrite import json_graph
import requests
import facebook 
import json

token='EAACEdEose0cBAMsRp6SwJ9jwiAaysRXaZAeLk9JF1HEdbz1Rx3dreqbYBHgltRUxwbcgwdZBA6lyuE3qyriHh2IvYUZCGmVXbY2liTjgtLwBk44SjFoMu9u520Ps7ZB0rYoVPtTLRfJZBnVUNzT7jVFr8427X8DifswJEdtOJEler8fWDEijj5nsCdR7e7UwZD'
g = facebook.GraphAPI(access_token = token)


friends = [ (friend['id'], friend['name'],)
	for friend in g.get_connections(id = 'me', connection_name = 'friends')['data'] ]
	
url = 'https://graph.facebook.com/%s?fields=context.fields%%28mutual_friends%%29&access_token=%s'

mutual_friends = {}

# This loop spawns a separate request for each iteration, so
# it may take a while.
for friend_id, friend_name in friends:
    r = requests.get(url % (friend_id, token,) )
    print json.loads(r.content)
    response_data = json.loads(r.content)['context']['mutual_friends']['data']
    mutual_friends[friend_name] = [ data['name']
		for data in response_data ]

nxg = nx.Graph()

[ nxg.add_edge('me', mf) for mf in mutual_friends ]

[ nxg.add_edge(f1, f2)
	for f1 in mutual_friends
		for f2 in mutual_friends[f1] ]

# Serializing a NetworkX graph to a file for consumption by D3
nld = json_graph.node_link_data(nxg)
json.dump(nld, open('viz/force.json','w'))
