#!/usr/bin/env python

import sys
import urllib2
import xml.etree.ElementTree as ET

from config import api_key, default_user, api_url

try:
    user = sys.argv[1]
except IndexError:
    user = default_user

# print user

result = urllib2.urlopen("%s/2.0/?method=user.getrecenttracks&limit=1&user=%s&api_key=%s" % (api_url, user, api_key)).read()
dom = ET.fromstring(result)

artist = dom.find("recenttracks/track/artist").text
song = dom.find("recenttracks/track/name").text

print "%s - %s" % (artist, song)
