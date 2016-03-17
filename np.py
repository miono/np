#!/usr/bin/env python

import sys
import urllib2
import json

from config import api_key, default_user, api_url

try:
    user = sys.argv[1]
except IndexError:
    user = default_user

result = urllib2.urlopen("%s/2.0/?method=user.getrecenttracks&limit=1&format=json&user=%s&api_key=%s" % (api_url, user, api_key))
data = json.load(result)

artist = data['recenttracks']['track'][0]['artist']['#text']
song = data['recenttracks']['track'][0]['name']


if data['recenttracks']['track'][0]['@attr']['nowplaying']:
    print "%s is listening to: %s - %s" % (user, artist, song)
else:
    print "%s last listened to: %s - %s" % (user, artist, song)
