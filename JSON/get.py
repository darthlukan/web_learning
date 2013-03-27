#!/usr/bin/env python2

import sys
import json

file = sys.argv[1]
json_data = open(file)
data = json.load(json_data)
webservlet = data['web-app']['servlet']

counter = 0

for i in webservlet:
    counter += 1
    print 'servlet-name:', i['servlet-name']
print "There are a total of %i servlet-names." % counter

json_data.close()