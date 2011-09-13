#!/usr/bin/env python

import httplib
import re
from Joke import Joke

def displaymatch(match):
        if match is None:
            return None
        return '<Match: %r, groups=%r>' % (match.group(), match.groups())

h = httplib.HTTPConnection('www.vayarisa.com')
h.request('GET', '/chiste_aleatorio.php')
resp = h.getresponse()
data = resp.read()

data = data.replace("<br />", "")

regexp = ".*>(.+)</font></u></h1><p><i>(.+)</i></p><a"
pattern = re.compile(regexp, re.S|re.M)

m = pattern.match(data)

j = Joke(m.group(1), m.group(2))
print unicode(str(j), 'iso-8859-1')
