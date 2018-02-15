import facebook
import json

# A helper function to pretty-print Python objects as JSON
def pp(o):
        print json.dumps(o, indent = 1)

# Create a connection to the Graph API with your access token
token = 'EAACEdEose0cBAFkK92V0u65FMZAx4zqFlNfFmViHvUcqC4yGe5jl6yFC2sRJpoomaZA0uD52CRB4C6VsZAmDAggLwu2lICV1TXiA2ElGDx7L4KIhIeZAq7wX0ZB3HfClBbOkYqCTc0jodcuZBEVEf7BLXI7cE0FDx038AfHgEWfm8SzjtCfrRkDtAANC9KxZB8ZD'
g = facebook.GraphAPI(access_token = token)

# Execute a few sample queries
print '---------------'
print 'Me'
print '---------------'
pp(g.get_object(id = 'me'))
print
print '---------------'
print 'My Friends'
print '---------------'
pp(g.get_connections(id = 'me', connection_name = 'friends'))
print
print '---------------'
print 'Pages about UVA'
print '---------------'
pp(g.request('search', {'q' : 'Universiteit van Amsterdam', 'type' : 'page', 'limit' : 5}))
print
print '---------------'
print 'Pages about VU'
print '---------------'
pp(g.request('search', {'q' : 'Vrije Universiteit Amsterdam', 'type' : 'page', 'limit' : 5}))

# Use the ids to query for likes
uva_id = '113928981951563'
vu_id = '116356121481'

# A quick way to format integers with commas every 3 digits
def int_format(n): return "{:,}".format(n)

#print "UVA likes:", int_format(g.get_object(uva_id)['likes'])
print "UVA likes:", int_format(g.get_object(id = uva_id, fields = 'likes')['likes'])
print "VU likes:", int_format(g.get_object(id = vu_id, fields = 'likes')['likes'])
